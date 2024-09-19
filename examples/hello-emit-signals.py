#!/usr/bin/python

######################################################################
#  Two classes that emit signals, and a parent that tie them
#  together.
#
#  2024-09-16 Mon
#  Dov Grobgeld <dov.grobgeld@gmail.com>
######################################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor, QPainter

# Define the TrafficLightWidget class
class TrafficLightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.blue_on = False
        self.red_on = False
        self.setFixedSize(100, 50)

    def paintEvent(self, event):  # override QWidget.paintEvent
        painter = QPainter(self)
        if self.blue_on:
            painter.setBrush(QColor('blue'))
        else:
            painter.setBrush(QColor('lightgray'))
        painter.drawEllipse(10, 10, 30, 30)

        if self.red_on:
            painter.setBrush(QColor('red'))
        else:
            painter.setBrush(QColor('lightgray'))
        painter.drawEllipse(60, 10, 30, 30)

    def set_blue_on(self, state):
        self.blue_on = state
        self.red_on = not state
        self.update()

    def set_red_on(self, state):
        self.red_on = state
        self.blue_on = not state
        self.update()

# Define the Pong class
class Pong(QObject):
    pong_signal = pyqtSignal()

    def your_turn(self):
        QTimer.singleShot(1000, self.emit_pong)

    def emit_pong(self):
        self.pong_signal.emit()

# Define the Ping class
class Ping(QObject):
    ping_signal = pyqtSignal()

    def your_turn(self):
        QTimer.singleShot(700, self.emit_ping)

    def emit_ping(self):
        self.ping_signal.emit()

# Define the Arena class
class Arena(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        # Create classes
        self.pong = Pong()
        self.ping = Ping()
        
        # Setup signal handlers
        self.pong.pong_signal.connect(self.handle_pong)
        self.ping.ping_signal.connect(self.handle_ping)
        
        # Let's get rolling!
        self.ping.ping_signal.emit()

    def initUI(self):
        self.label = QLabel('state', self)
        self.traffic_light = TrafficLightWidget()
        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(QApplication.instance().quit)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        
        traffic_light_layout = QHBoxLayout()
        traffic_light_layout.addStretch(1)
        traffic_light_layout.addWidget(self.traffic_light)
        traffic_light_layout.addStretch(1)
        
        layout.addLayout(traffic_light_layout)
        layout.addWidget(self.quit_button)
        
        self.setLayout(layout)
        self.setWindowTitle('Arena')
        self.show()

    def handle_pong(self):
        self.label.setText('Received pong')
        self.traffic_light.set_red_on(True)
        self.ping.your_turn()

    def handle_ping(self):
        self.label.setText('Received ping')
        self.traffic_light.set_blue_on(True)
        self.pong.your_turn()

# Main function to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    arena = Arena()
    sys.exit(app.exec_())
