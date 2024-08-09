#!/usr/bin/env python

######################################################################
#  An example of how to apply a stylesheet
#
#  2024-08-04 Sun
#  Dov Grobgeld <dov.grobgeld@gmail.com>
######################################################################

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton

# Fixed, or read from a resource file
myStyle = '''
QLabel { background-color : pink; color : black; }
#lupchi { background-color : lime; color : black; }
'''

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set style of label to be pink
        self.setStyleSheet(myStyle)

        # Create a layout and place two labels in it
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(self, text="Hello, World!")) # English
        layout.addWidget(QLabel(self, text="שלום עולם!‏"))     # Internationalization (i18n) support
        # Add a button of class lupchi
        layout.addWidget(QPushButton(self, text="I'm Lupchi!", objectName="lupchi"))

        # Set preferred size
        self.resize(320, 240)

app = QApplication([])
window = MyWidget()
window.show()
app.exec_()

