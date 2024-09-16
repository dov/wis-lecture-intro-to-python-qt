######################################################################
#  Model/view example in python qt.
#
#  The example shows updating the data changes its display.
#
#  2024-08-09 Fri
#  Dov Grobgeld <dov.grobgeld@gmail.com>
######################################################################

import sys
from PyQt5.QtCore import Qt, QAbstractListModel, QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow, QListView, QVBoxLayout, QWidget, QPushButton
import random

class SimpleListModel(QAbstractListModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = data or []

    def rowCount(self, parent=None):  # override
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):  # override
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            return self._data[index.row()]
        return None

    def setData(self, index, value, role=Qt.EditRole): # override
        if index.isValid() and role == Qt.EditRole:
            self._data[index.row()] = value
            self.dataChanged.emit(index, index, [Qt.DisplayRole])
            return True
        return False

    def flags(self, index): # override
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Model-View Example with Data Modification")

        # Create a central widget and set a layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Create a list view and set the model
        self.list_view = QListView()
        self.model = SimpleListModel(["Item 1", "Item 2", "Item 3"])
        self.list_view.setModel(self.model)
        layout.addWidget(self.list_view)

        # Create a button to modify the data
        self.button = QPushButton("Update Data")
        self.button.clicked.connect(self.updateData)
        layout.addWidget(self.button)

        self.resize(300, 200)

    # A custom function to show how to update the display data
    # by setting the model.
    def updateData(self):
        for i in range(self.model.rowCount()):
            val = random.randint(1,100)
            self.model.setData(self.model.index(i), f'Updated data {val}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
