######################################################################
#  Demo of form layout and of a dialog including a graphics view.
#
#  2024-08-07 Wed
#  Dov Grobgeld <dov.grobgeld@gmail.com>
######################################################################

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFormLayout,
                             QLineEdit, QPushButton, QDialog, QVBoxLayout,
                             QGraphicsView, QGraphicsScene, QGraphicsTextItem,
                             QGraphicsPathItem)
from PyQt5.QtGui import QFont, QPixmap, QColor, QPainterPath, QPen
from PyQt5.QtCore import Qt, QPointF

class BusinessCardDialog(QDialog):
    def __init__(self, name, phone, occupation, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Business Card")
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        graphics_view = QGraphicsView()
        layout.addWidget(graphics_view)
        
        scene = QGraphicsScene()
        graphics_view.setScene(scene)
        
        # Note use of html!
        text = f"""
        <div style="font-family: Candara; font-size: 16pt; color: #191970">
            <p>Name: <b>{name}</b></p>
            <p>Phone: <b>{phone}</b></p>
            <p>Occupation: <b>{occupation}</b></p>
        </div>
        """
        text_item = QGraphicsTextItem(text)
        text_item.setHtml(text)
        scene.addItem(text_item)
        
        self.resize(640, 480)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Business Card Form")
        
        layout = QFormLayout()
        self.setLayout(layout)
        
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Name")
        self.phone_edit = QLineEdit()
        self.phone_edit.setPlaceholderText("+972-59999999")
        self.occupation_edit = QLineEdit()
        self.occupation_edit.setPlaceholderText("Occupation")
        
        layout.addRow("Name:", self.name_edit)
        layout.addRow("Phone Number:", self.phone_edit)
        layout.addRow("Occupation:", self.occupation_edit)
        
        self.submit_button = QPushButton("Create Business Card")
        self.submit_button.clicked.connect(self.show_business_card)
        layout.addWidget(self.submit_button)
    
    def show_business_card(self):
        name = self.name_edit.text()
        phone = self.phone_edit.text()
        occupation = self.occupation_edit.text()
        
        dialog = BusinessCardDialog(name, phone, occupation, self)
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
