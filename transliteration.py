#!/usr/bin/env python3


import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from separate_syllables import separateSyllables
from create_telugu_word import createTeluguWord


class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.in_out_box = TextEdit()
        self.in_out_box.setPlaceholderText("Enter text in English and "
                                           "press Space to convert it to Telugu")
        self.in_out_box.setFont(QFont('garuda', 15))
        self.in_out_box.space_pressed.connect(self.convertToTelugu)

        self.cursor = self.in_out_box.textCursor()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.in_out_box)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)
        self.setWindowTitle("English to Telugu Converter")
        self.setMinimumSize(700, 500)
        self.show()

    def convertToTelugu(self):
        text = self.in_out_box.toPlainText()[:self.cursor.position()-1]
        word = text.split()[-1]
        if word.isalpha():
            telugu_word = createTeluguWord(separateSyllables(word))
            self.cursor.insertText(telugu_word)
        else:
            return


class TextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)

    space_pressed = pyqtSignal()

    def keyPressEvent(self, event):
        super(TextEdit, self).keyPressEvent(event)
        if event.key() in (Qt.Key_Space,):
                           # Qt.Key_Enter,
                           # Qt.Key_Return,
                           # Qt.Key_Period):
            self.space_pressed.emit()
        elif event.key() == Qt.Key_Escape:
            self.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = Form()
    app.exec_()
# def event(self, event):
#     if event.type() == QEvent.KeyPress:
#         cursor = self.textCursor()
#         if event.key() == Qt.Key_Space:
#             cursor.insertText(" ")
#             print("space pressed")
#             return True
#         elif event.key() == Qt.Key_Escape:
#             self.clear()
#             return True
#         elif event.key() == Qt.Key_Tab:
#             cursor.insertText(" ")
#             return True
#     return QTextEdit.event(self, event)
