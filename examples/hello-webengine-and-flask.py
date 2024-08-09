######################################################################
#  Run this script to start a Flask server and a PyQt5
#  application that displays a web page served by the Flask server.
#
#  The Flask server is started in a separate thread, and the PyQt5
#  application is started in the main thread.
#
#  Dov Grobgeld <dov.grobgeld@gmail.com>
#  2024-08-04 Sun
######################################################################

import sys
import threading
import random
import string
from flask import Flask, request, render_template_string, abort
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

# Prevent anybody speaking to the backend by generate a secret token
SECRET_TOKEN = ''.join(random.choices(string.ascii_letters + string.digits, k=32))

# Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    token = request.args.get('token')
    if token != SECRET_TOKEN:
        abort(403)  # Forbidden

    result = None
    if request.method == 'POST':
        try:
            number = float(request.form['number'])
            result = number ** 2
        except ValueError:
            result = "Invalid input. Please enter a number."

    return render_template_string('''
        <!doctype html>
        <title>Square a Number</title>
        <h1>Enter a number to square:</h1>
        <form method="post">
            <input type="text" name="number">
            <input type="submit" value="Submit">
        </form>
        {% if result is not none %}
            <h2>Result: {{ result }}</h2>
        {% endif %}
    ''', result=result)

def run_flask(port):
    app.run(port=port, debug=False, host='127.0.0.1')

# PyQt5 app with QtWebEngine
class MainWindow(QWidget):
    def __init__(self, port):
        super().__init__()

        self.port = port
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 and Flask Example')

        layout = QVBoxLayout()

        self.webview = QWebEngineView()
        self.webview.setUrl(QUrl(f'http://127.0.0.1:{self.port}/?token={SECRET_TOKEN}'))
        layout.addWidget(self.webview)

        self.setLayout(layout)

def run_pyqt(port):
    app = QApplication(sys.argv)
    window = MainWindow(port)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    # Generate a random port
    port = random.randint(1024, 65535)

    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask, args=(port,))
    flask_thread.daemon = True
    flask_thread.start()

    # Start PyQt5 UI in the main thread
    run_pyqt(port)
