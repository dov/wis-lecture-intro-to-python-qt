import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import pyqtgraph as pg
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scientific XY Graph with PyQt")
        self.setGeometry(100, 100, 800, 600)
        
        # Create a central widget and set a layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # Create a PlotWidget
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)
        
        # Generate some data
        x = np.linspace(0, 10, 1000)
        y = np.sin(x)
        
        # Plot the data
        self.plot_widget.plot(x, y, pen=pg.mkPen(color='b', width=2))
        
        # Set labels and title
        self.plot_widget.setLabel('left', 'Y-Axis', units='A')
        self.plot_widget.setLabel('bottom', 'X-Axis', units='s')
        self.plot_widget.setTitle('Scientific XY Graph')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
