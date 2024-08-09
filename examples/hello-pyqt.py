#!/usr/bin/env python

######################################################################
#  A hello world program in PyQt5
#
#  2024-08-04 Sun
#  Dov Grobgeld <dov.grobgeld@gmail.com>
######################################################################

from PyQt5.QtWidgets import QApplication, QLabel, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__() # Call parentconstructor
        # Set the window title
        self.setWindowTitle("Hello, World!")
        self.label = QLabel(self, text="Hello, World!")

        # Set preferred size
        self.resize(320, 240)

app = QApplication([])  # Create application before widgets
window = MyWidget()     # Each application has one widget
window.show()           # Show it
app.exec_()             # Enter main loop

