######################################################################
# Create a QGraphicsView with a "car" and allow moving it around with
# the mouse
#
# 2024-08-04 Sun
# Dov Grobgeld <dov.grobgeld@gmail.com>
######################################################################

import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPolygonItem, QGraphicsItem
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QBrush, QPen, QPolygonF

class CarItem(QGraphicsPolygonItem):
    def __init__(self):
        car_outline = QPolygonF([
            QPointF(0, 50), QPointF(15,50), QPointF(30, 20), QPointF(80, 20), QPointF(100, 50),  
            QPointF(100, 80), QPointF(0, 80)  
        ])

        super().__init__(car_outline)
        self.setAcceptHoverEvents(True)  # Enable hover events

    def hoverEnterEvent(self, event):
        self.setBrush(QBrush(Qt.red))  # Change color on hover
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setBrush(QBrush(Qt.blue))  # Change color back
        super().hoverLeaveEvent(event)

class MainWindow(QGraphicsView):
    def __init__(self):
        super().__init__()

        # Create a scene
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Create a custom polygon item
        polygon_item = CarItem()
        polygon_item.setBrush(QBrush(Qt.blue))
        polygon_item.setPen(QPen(Qt.black))
        self.scene.addItem(polygon_item)

        # Enable transformations
        polygon_item.setFlag(QGraphicsItem.ItemIsMovable)
        polygon_item.setFlag(QGraphicsItem.ItemIsSelectable)
        polygon_item.setFlag(QGraphicsItem.ItemIsFocusable)

        self.resize(640, 480)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
