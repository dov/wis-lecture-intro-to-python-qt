######################################################################
#  Create a webview and load a page from the web.
#
#  2024-08-04 Sun
#  Dov Grobgeld
######################################################################

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

# import QUrl from PyQt5.QtCore
from PyQt5.QtCore import QUrl

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://weizmann.ac.il"))
        self.setCentralWidget(self.browser)

app = QApplication([])
window = MyMainWindow()
window.show()
app.exec_()
