from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class Hello_World(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        # setting up layout
        layout = QGridLayout() # QVBoxLayout QHBoxLayout

        # creating the widgets
        self.label = QLabel("Hell World!") # Label
        line_edit = QLineEdit() # Textbox
        button = QPushButton("Close") # Button

        # Drawing layout
        layout.addWidget(self.label, 0,0) # Column, Row
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)

        self.setLayout(layout)

        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.change_text_label)

    def change_text_label(self, text):
        self.label.setText(text)

app = QApplication(sys.argv)
dialog = Hello_World()
dialog.show()
sys.exit(app.exec_())
