from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThreadPool

from gui.windows import IntroWindow
from gui.loaders import ImageLoader, ModelLoader


class UiStartWindow(object):
    def setupUi(self, start_window):
        self.start_window = start_window
        self.start_window.setObjectName("start_window")
        self.start_window.resize(644, 677)
        self.start_window.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.start_window.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(start_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 180, 351, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_menu_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_menu_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.main_menu_layout.setContentsMargins(12, 0, 12, 0)
        self.main_menu_layout.setSpacing(10)
        self.main_menu_layout.setObjectName("main_menu_layout")
        self.image_load_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.image_load_button.setIconSize(QtCore.QSize(20, 19))
        self.image_load_button.setObjectName("image_load_button")
        self.main_menu_layout.addWidget(self.image_load_button)

        self.video_load_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.video_load_button.setIconSize(QtCore.QSize(20, 19))
        self.video_load_button.setObjectName("video_load_button")
        self.main_menu_layout.addWidget(self.video_load_button)

        start_window.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(start_window)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.start_window.setWindowTitle(_translate("start_window", "MainWindow"))
        self.image_load_button.setText(_translate("start_window", "CHECK IMAGE"))
        self.video_load_button.setText(_translate("start_window", "CHECK VIDEO"))


class StartWindow(UiStartWindow):
    def __init__(self, start_window):
        self.setupUi(start_window)
        self.window = QtWidgets.QMainWindow()
        self.intro_window = IntroWindow(self.window, start_window)
        self.start_window.hide()
        self.threadpool = QThreadPool()
        self.model_loader = ModelLoader()
        self.threadpool.start(self.model_loader)
        self.model_loader.signals.finished.connect(
            lambda: self.intro_window.after_model_load(self.model_loader.trained_model)
        )
        self.image_editor_window = None

        self.image_load_button.clicked.connect(self.load_user_image)
        self.video_load_button.clicked.connect(self.load_user_video)

    def hide_window(self):
        self.intro_window.intro_window.show()

    def load_user_image(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        image_path, _ = QtWidgets.QFileDialog.getOpenFileName(self.start_window, "QFileDialog.getOpenFileName()", "",
                                                              "Image files (*.jpg *.png)", options=options)
        user_image = ImageLoader(image_path)

    def load_user_video(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        # TODO extend options of video
        video_path, _ = QtWidgets.QFileDialog.getOpenFileName(self.start_window, "QFileDialog.getOpenFileName()", "",
                                                              "Video files (*.mp4)", options=options)

    def start(self):
        self.intro_window.start()
