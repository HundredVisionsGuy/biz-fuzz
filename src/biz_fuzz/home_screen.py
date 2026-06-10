"""
home_screen.py
by HundredVisionsGuy
The home screen - welcomes the user and pulls any filenames into a link
"""

import controller
from PySide6.QtWidgets import (
    QLabel,
    QListWidget,
    QVBoxLayout,
    QWidget)

class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.title_label = QLabel("About")
        self.title_label.setProperty("cssClass",
                                     "title")
        
        welcome_label = QLabel("Welcome to the Bizz Fuzz App!")
        self.description_label = QLabel("")
        # Create a list of first 5 todo lists (if there are any)
        self.my_todo_lists = QListWidget()
        self.populate_todo_items()

        # add widgets
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(welcome_label)
        self.layout.addWidget(self.description_label)
        self.layout.addWidget(self.my_todo_lists)
        self.setLayout(self.layout)
    
    def populate_todo_items(self):
        todo_items = controller.get_todo_lists()
        if not todo_items:
            no_items = "To get started, click the new button to create a todo"
            no_items += " list."
            self.description_label.setText(no_items)