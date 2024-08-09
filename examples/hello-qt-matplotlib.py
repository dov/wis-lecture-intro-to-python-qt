import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matplotlib Embedded in PyQt")
        self.setGeometry(100, 100, 800, 600)
        
        # Create a central widget and set a layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # Create a Matplotlib canvas
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        layout.addWidget(self.canvas)

        quitButton = QPushButton("Quit")
        quitButton.clicked.connect(self.close)
        layout.addWidget(quitButton)

        
        # Generate some data
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        
        # Plot the data
        self.canvas.axes.plot(x, y)
        self.canvas.axes.set_xlabel('X-Axis')
        self.canvas.axes.set_ylabel('Y-Axis')
        self.canvas.axes.set_title('Scientific XY Graph')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
