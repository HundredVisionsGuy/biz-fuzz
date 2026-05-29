"""
calendar_screen.py
by HundredVisionsGuy
A screen to display custom calendar
"""

from PySide6.QtWidgets import (
    QCalendarWidget,
    QLabel,)
from screen_widget import ScreenWidget

class CalendarScreen(ScreenWidget):
    def __init__(self):
        super().__init__()
        self.title_label.setText("Your calendar.")

        calendar = QCalendarWidget()

        # add widgets
        self.layout.addWidget(calendar)