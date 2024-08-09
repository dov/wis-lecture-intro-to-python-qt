# Load the ui file mainwin.ui and use it to display the window

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        loadUi("mainwin.ui", self)

        # Connect using the names in the ui file
        self.actionQuit.triggered.connect(self.close)  # Name from uifile
        self.actionLoad.triggered.connect(self.load_image)
        self.actionAbout.triggered.connect(self.show_about)

    def show_about(self):
        QMessageBox.information(self, "About", "Hello UI!")

    def load_image(self):
        # create an error message box
        QMessageBox.critical(self, "Error", "Not implemented yet")

app = QApplication([])
window = MyMainWindow()
window.show()
app.exec_()

