"""
calendar_screen.py
by HundredVisionsGuy
A screen to display custom calendar
"""

from PySide6.QtWidgets import (
    QCalendarWidget,
    QLabel,
    QVBoxLayout,
    QWidget)

class CalendarScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.title_label = QLabel("Your calendar.")
        self.title_label.setProperty("cssClass",
                                     "title")
        calendar = QCalendarWidget()

        # add widgets
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(calendar)
        self.setLayout(self.layout)