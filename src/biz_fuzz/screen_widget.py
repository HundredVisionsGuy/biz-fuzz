"""
screen_widget.py
by HundredVisionsGuy
A base class for each screen in the stacked layout
"""

from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QVBoxLayout)


class ScreenWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.title_label = QLabel("")
        self.title_label.setProperty("cssClass",
                                     "title")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label)
        self.setLayout(self.layout)
