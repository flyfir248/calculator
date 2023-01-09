import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the user interface
        self.initUI()

    def initUI(self):
        # Create a widget to hold the display and buttons
        wid = QWidget(self)
        self.setCentralWidget(wid)

        # Create the display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Create the buttons
        self.buttons = []
        for i in range(10):
            self.buttons.append(QPushButton(str(i)))

        self.add_button = QPushButton('+')
        self.sub_button = QPushButton('-')
        self.mul_button = QPushButton('*')
        self.div_button = QPushButton('/')
        self.dec_button = QPushButton('.')
        self.eval_button = QPushButton('=')
        self.clear_button = QPushButton('C')

        # Create the layout
        grid = QGridLayout()
        wid.setLayout(grid)
        grid.addWidget(self.display, 0, 0, 1, 4)

        for i in range(10):
            row = ((9 - i) // 3) + 1
            col = ((i - 1) % 3) + 1
            grid.addWidget(self.buttons[i], row, col)

        grid.addWidget(self.add_button, 4, 3)
        grid.addWidget(self.sub_button, 3, 3)
        grid.addWidget(self.mul_button, 2, 3)
        grid.addWidget(self.div_button, 1, 3)
        grid.addWidget(self.dec_button, 4, 2)
        grid.addWidget(self.eval_button, 4, 1)
        grid.addWidget(self.clear_button, 3, 1, 2, 1)

        # Set window properties
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 400)

        # Connect buttons to display
        for i in range(10):
            self.buttons[i].clicked.connect(lambda: self.add_to_display(self.buttons[i].text()))
        self.dec_button.clicked.connect(lambda: self.add_to_display(self.dec_button.text()))
        self.add_button.clicked.connect(lambda: self.add_to_display(self.add_button.text()))
        self.sub_button.clicked.connect(lambda: self.add_to_display(self.sub_button.text()))
        self.mul_button.clicked.connect(lambda: self.add_to_display(self.sub_button.text()))

        def add_to_display(self, text):
            self.display.setText(self.display.text() + text)

        def evaluate_expression(self):
            try:
                result = str(eval(self.display.text()))
            except Exception:
                result = 'ERROR'
            self.display.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())