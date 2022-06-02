import sys

from PyQt5 import QtWidgets

from gui.windows.start_window import StartWindow


def start():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    start_window = StartWindow(window)
    start_window.start()
    sys.exit(app.exec_())
