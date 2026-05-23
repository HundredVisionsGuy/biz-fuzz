"""
screen_widget.py
by HundredVisionsGuy
A base class for each screen in the stacked layout
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout


class ScreenWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
