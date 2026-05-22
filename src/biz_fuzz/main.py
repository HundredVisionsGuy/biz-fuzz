"""
basic_app.py
by HundredVisionsGuy
A demo of the most basic input/output: labels, text inputs, and buttons.
"""

import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QCheckBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To Do List")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Create a Todo list by adding todo items.")

        # Widgets to create a Todo Item
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("What do you want to do?")

        self.priority_label = QLabel("Set Priority Level ")
        self.priority_list = QListWidget()
        self.priority_list.addItems(["High", "Medium", "Low"])
        self.priority_list.setFlow(QListWidget.LeftToRight)
        self.priority_list.setCurrentRow(1)

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
        layout.addWidget(self.name_input)
        layout.addWidget(self.priority_label)
        layout.addWidget(self.priority_list)
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

        todo_priority = self.priority_list.currentItem().text()
        self.priority_list.clearSelection()

        todo_string = f"{todo_name} -> {todo_priority}"
        todo_button = QCheckBox(todo_string)
        self.todo_list.addButton(todo_button)
        self.todo_layout.addWidget(todo_button)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()