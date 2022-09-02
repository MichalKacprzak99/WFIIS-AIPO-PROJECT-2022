from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot
from model.predictor import Predictor


class GeoLocalizatorSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    """
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)


class GeoLocalizator(QRunnable):
    data = None

    def __init__(self, graphic_data):
        super(GeoLocalizator, self).__init__()

        self.graphic_data = graphic_data
        self.signals = GeoLocalizatorSignals()

        self.predictor = Predictor()

    @pyqtSlot()
    def run(self):

        """
        Your code goes in this function
        """
        res = self.predictor.predict_for_images(self.graphic_data)

        # normalize
        s = 0
        for k in res:
            s += res[k]
        for k in res:
            res[k] = res[k] / s

        print("RESULT: ")  
        print(res)

        try:
            if not res:
                self.data = {"Nie wiem ¯\\_(ツ)_/¯ ": 1.0}
            else:
                self.data = res
        finally:
            self.signals.finished.emit()
