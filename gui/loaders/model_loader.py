from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot
from tensorflow.keras import models


class ModelLoaderSignals(QObject):
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


class ModelLoader(QRunnable):
    trained_model = None

    def __init__(self):
        super(LoadModel, self).__init__()

        self.signals = ModelLoaderSignals()

    def predict(self, img):
        return self.trained_model.predict(img)

    @pyqtSlot()
    def run(self):

        """
        Your code goes in this function
        """

        try:
            # self.trained_model = models.load_model("../model/model_trained_animals_batch_16_imagenet.hdf5")
            self.trained_model = True
        except:
            self.trained_model = None
        finally:
            self.signals.finished.emit()  # Done
