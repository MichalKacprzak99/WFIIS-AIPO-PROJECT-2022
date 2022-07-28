from typing import Optional

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThreadPool

from .geo_localizator import GeoLocalizator


class UiResultsWindow(object):
    def setupUi(self, results_window):
        self.results_window = results_window

        self.results_window.setObjectName("ResultsWindow")
        self.results_window.resize(891, 726)
        self.centralwidget = QtWidgets.QWidget(self.results_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.process_label = QtWidgets.QLabel(self.centralwidget)
        self.process_label.setGeometry(QtCore.QRect(280, 50, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.process_label.setFont(font)
        self.process_label.setAlignment(QtCore.Qt.AlignCenter)
        self.process_label.setObjectName("label")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(320, 120, 256, 461))
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setObjectName("listWidget")
        self.results_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(results_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 26))
        self.menubar.setObjectName("menubar")
        self.results_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(results_window)
        self.statusbar.setObjectName("statusbar")
        self.results_window.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(results_window)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.results_window.setWindowTitle(_translate("ResultsWindow", "ResultsWindow"))
        self.label.setText(_translate("ResultsWindow", "Results"))
        self.process_label.setText(_translate("ResultsWindow", "processing"))
        __sortingEnabled = self.listWidget.isSortingEnabled()


class ResultsWindow(UiResultsWindow):
    def __init__(self, window, start_window, graphic_data):
        self.start_window = start_window
        self.setupUi(window)
        self.window = window

        self.threadpool = QThreadPool()
        self.geo_localizator = GeoLocalizator(graphic_data=graphic_data)

        self.threadpool.start(self.geo_localizator)
        self.geo_localizator.signals.finished.connect(
            lambda: self.after_localize(self.geo_localizator.data)
        )

    def show(self):
        self.results_window.show()

    def after_localize(self, data: Optional[dict] = None):
        _translate = QtCore.QCoreApplication.translate

        if not data:
            ...
            self.process_label.setText(_translate("intro_window", "Failed to process image/video"))
        else:
            ...
            self.process_label.hide()
            for country, percentage in data.items():
                item = QtWidgets.QListWidgetItem(f"{country}: {percentage * 100} %")
                self.listWidget.addItem(item)
