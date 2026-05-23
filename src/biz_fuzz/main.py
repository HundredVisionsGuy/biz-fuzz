"""
main.py
by HundredVisionsGuy
A TODO management app. A screen with a navbar and a Qstacked Layout for the various
features (view list, create list, calendar view)
"""

import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
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
        nav_widget = QWidget()
        nav_layout = QHBoxLayout()
        for option in ["home", "new", "my tasks", "calendar"]:
            btn = QPushButton(option)
            self.nav_group.addButton(btn)
            nav_layout.addWidget(btn)
        nav_widget.setLayout(nav_layout)

        title_label = QLabel("Create a Todo list by adding todo items.")

        # Widgets to create a Todo Item
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("What do you want to do?")

        self.priority_label = QLabel("Set Priority Level ")

        # NOTE: a QButtonGroup is not a widget
        self.priority_group = QButtonGroup()
        self.priority_group.setExclusive(False)

        # We have to set a widget for the QButtonGroup
        priority_widget = QWidget()
        priority_layout = QVBoxLayout()

        # Add buttons to the group and the layout
        for option in ["High", "Medium", "Low"]:
            btn = QRadioButton(option)
            self.priority_group.addButton(btn)
            priority_layout.addWidget(btn)

        # Add the layout to the widget
        priority_widget.setLayout(priority_layout)

        add_todo_button = QPushButton("Add Item")
        add_todo_button.clicked.connect(self.add_todo_item)

        # Output Section
        output_label = QLabel("Your ToDo List")
        self.todo_list = QButtonGroup()
        self.todo_list.setExclusive(False)
    
        # Container for todo items
        self.todo_container = QWidget()
        self.todo_layout = QVBoxLayout()
        self.todo_container.setLayout(self.todo_layout)

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(nav_widget)
        layout.addWidget(self.name_input)
        layout.addWidget(self.priority_label)
        layout.addWidget(priority_widget)
        layout.addWidget(add_todo_button)
        layout.addWidget(output_label)
        layout.addWidget(self.todo_container)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
    
    def add_todo_item(self):
        todo_name = self.name_input.text()
        self.name_input.setText("")

        checked_priority = self.priority_group.checkedButton()
        todo_priority = checked_priority.text()
        checked_priority.setChecked(False)

        todo_string = f"{todo_name} -> {todo_priority}"
        todo_button = QCheckBox(todo_string)
        self.todo_list.addButton(todo_button)
        self.todo_layout.addWidget(todo_button)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()