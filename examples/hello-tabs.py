import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel

class TabDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multipage with Horizontal Tabs")
        self.setGeometry(100, 100, 600, 400)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create QTabWidget
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        # Create tabs
        self.create_tabs()
    
    def create_tabs(self):
        # First tab
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QLabel("Content of Tab 1"))
        tab1.setLayout(tab1_layout)
        
        # Second tab
        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel("Content of Tab 2"))
        tab2.setLayout(tab2_layout)
        
        # Third tab
        tab3 = QWidget()
        tab3_layout = QVBoxLayout()
        tab3_layout.addWidget(QLabel("Content of Tab 3"))
        tab3.setLayout(tab3_layout)
        
        # Add tabs to QTabWidget
        self.tabs.addTab(tab1, "Tab 1")
        self.tabs.addTab(tab2, "Tab 2")
        self.tabs.addTab(tab3, "Tab 3")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = TabDemo()
    demo.show()
    sys.exit(app.exec_())
