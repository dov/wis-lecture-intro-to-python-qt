# This is a simple example of a PyQt5 application that asks
# for the user's name and then greets them with a message box.

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout and place two labels in it
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(self, text="What is your name?"))
        self.name = QLineEdit(self)
        layout.addWidget(self.name)
        button = QPushButton(self, text="Click me")
        button.clicked.connect(self.on_button_click)
        layout.addWidget(button)

        # Set preferred size
        self.resize(320, 240)

    def on_button_click(self):
        QMessageBox.information(self, "Hello", f"Hello, {self.name.text()}!")


app = QApplication([])
window = MyWidget()

window.show()

app.exec_()
