"""
main.py
by HundredVisionsGuy
A TODO management app. A screen with a navbar and a Qstacked Layout for the various
features (view list, create list, calendar view)
"""

from create_screen import CreateScreen
from calendar_screen import CalendarScreen
import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Do It app")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        self.nav_group = QButtonGroup(self)
        self.nav_group.buttonClicked.connect(self.nav_selected)
        nav_widget = QWidget()
        nav_layout = QHBoxLayout()
        for option in ["home", "new", "my tasks", "calendar"]:
            btn = QPushButton(option)
            self.nav_group.addButton(btn)
            nav_layout.addWidget(btn)
        nav_widget.setLayout(nav_layout)

        self.screen_layout = QStackedLayout()
        
        add_screen = CreateScreen()
        self.screen_layout.addWidget(add_screen)

        calendar_screen = CalendarScreen()
        self.screen_layout.addWidget(calendar_screen)

        layout.addWidget(nav_widget)
        layout.addLayout(self.screen_layout)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
    
    def nav_selected(self, button):
        match button.text():
            case "calendar":
                self.screen_layout.setCurrentIndex(1)
            case "new":
                self.screen_layout.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()