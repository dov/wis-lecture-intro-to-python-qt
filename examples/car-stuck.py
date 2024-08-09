# Create a QGraphicsView with a "car" and allow moving it around
import sys
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsPolygonItem, QGraphicsItem,
                             QWidget, QVBoxLayout, QPushButton)
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QBrush, QPen, QPolygonF
import time

class CarItem(QGraphicsPolygonItem):
    def __init__(self):
        car_outline = QPolygonF([
            QPointF(0, 50), QPointF(15,50), QPointF(30, 20), QPointF(80, 20),
            QPointF(100, 50), QPointF(120, 50), QPointF(120, 80), QPointF(0, 80)  
        ])

        super().__init__(car_outline)
        self.setAcceptHoverEvents(True)  # Enable hover events

    def hoverEnterEvent(self, event):
        self.setBrush(QBrush(Qt.red))  # Change color on hover
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setBrush(QBrush(Qt.blue))  # Change color back
        super().hoverLeaveEvent(event)

class CarView(QGraphicsView):
    def __init__(self):
        super().__init__()

        # Create a scene
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Create a custom polygon item
        self.car = CarItem()
        self.car.setBrush(QBrush(Qt.blue))
        self.car.setPen(QPen(Qt.black))
        self.scene.addItem(self.car)

        # Enable transformations
        self.car.setFlag(QGraphicsItem.ItemIsMovable)
        self.car.setFlag(QGraphicsItem.ItemIsSelectable)
        self.car.setFlag(QGraphicsItem.ItemIsFocusable)

    def moveCar(self, pos):
        # Move the car to the new position
        self.car.setPos(pos, 200)
        

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Create a layout and place two labels in it
        layout = QVBoxLayout(self)
        self.car = CarView()
        layout.addWidget(self.car)
        button = QPushButton(self, text="Move!")
        button.clicked.connect(self.onMoveClicked)
        layout.addWidget(button)
        self.startPos = 50
        self.car.moveCar(self.startPos)

        self.resize(640, 480)

    def onMoveClicked(self):
        for i in range(30):
            self.car.moveCar(self.startPos + i*10)
            time.sleep(0.1)       # This grabs the event loop and blocks the GUI!

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
