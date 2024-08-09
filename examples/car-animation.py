# A template of a simple application

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from pathlib import Path

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.label = QLabel(self.central_widget)
        self.layout.addWidget(self.label)

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        self.load_action = QAction("Load", self)
        self.load_action.triggered.connect(self.load_image)
        self.file_menu.addAction(self.load_action)

        self.file_menu.addSeparator()
        self.quit_action = QAction("Quit", self)
        self.quit_action.triggered.connect(self.close)
        self.file_menu.addAction(self.quit_action)

        # Set the initial size of the window
        self.resize(640, 480)

        self.label.setScaledContents(True)
        

    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            pixmap = QPixmap(file_name)
            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio))
            # When loaded show in the status bar for 2 second "Loaded image"
            self.statusBar().showMessage(f"Loaded {Path(file_name).name}", 2000)
            

app = QApplication(sys.argv)
window = MyMainWindow()
window.show()

app.exec_()
