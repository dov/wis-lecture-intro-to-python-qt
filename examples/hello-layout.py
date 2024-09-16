#!/usr/bin/env python

######################################################################
#  An example of how to use a layout to place two labels in a window.
#
#  2024-08-04 Sun
#  Dov Grobgeld <dov.grobgeld@gmail.com>
######################################################################

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout 
        layout = QVBoxLayout()

        # Attach it to self
        self.setLayout(layout)

        # Crete widgets while adding them to the layout
        layout.addWidget(QLabel(self, text="Hello, World!")) # English
        layout.addWidget(QLabel(self, text="שלום עולם!‏"))     # Internationalization (i18n) support

        # Set initial size
        self.resize(320, 240)

app = QApplication([])
window = MyWidget()
window.show()
app.exec_()

