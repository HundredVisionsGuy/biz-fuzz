"""
main.py
by HundredVisionsGuy
A TODO management app. A screen with a navbar and a Qstacked Layout for the various
features (view list, create list, calendar view)
"""

from create_screen import CreateScreen
from calendar_screen import CalendarScreen
from home_screen import HomeScreen
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)

stylesheet = """
QMainWindow {
    background-color: #aaccee;
}
QLabel[cssClass="title"] {
    font-size:32px;
    color: #4e6e5d;
    font-weight: bold;
}
"""
font = QFont("Poiret One", 16)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Do It app")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 740)
        self.set_fonts()

        layout = QVBoxLayout()

        app_title = QLabel("Bizz Fuzz App")
        app_title.setFont(QFont("Montserrat", 32, 800))


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
        
        home_screen = HomeScreen()
        add_screen = CreateScreen()
        self.screen_layout.addWidget(home_screen)
        self.screen_layout.addWidget(add_screen)

        calendar_screen = CalendarScreen()
        self.screen_layout.addWidget(calendar_screen)

        # center vertically by adding stretch at the beginning and the end
        layout.addSpacing(20)
        layout.addWidget(app_title)
        layout.addWidget(nav_widget)
        layout.addLayout(self.screen_layout)
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
    
    def nav_selected(self, button):
        match button.text():
            case "calendar":
                self.screen_layout.setCurrentIndex(2)
            case "new":
                self.screen_layout.setCurrentIndex(1)
            case "home":
                self.screen_layout.setCurrentIndex(0)

    def set_fonts(self):
        font_dir = "src/biz_fuzz/resources/fonts/"
        header_font_name = "PoiretOne-Regular.ttf"
        body_font_name = "Raleway-VariableFont_wght.ttf"
        header_font_path = font_dir + header_font_name
        body_font_path = font_dir + body_font_name
        self.check_font_success(header_font_path)
        self.check_font_success(body_font_path)

    def check_font_success(self, font_path):
        success = QFontDatabase.addApplicationFont(font_path)
        if success == -1:
            print(f"there was a problem loading {font_path}")

        


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    # Styles


    app.setStyleSheet(stylesheet)
    app.setFont(font)

    window = MainWindow()
    window.show()

    app.exec()