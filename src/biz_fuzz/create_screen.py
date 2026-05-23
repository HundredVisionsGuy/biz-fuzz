"""
create_screen.py
by HundredVisionsGuy
A base class for each screen in the stacked layout
"""

from PySide6.QtWidgets import (
    QButtonGroup,
    QCheckBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QWidget)
from screen_widget import ScreenWidget

class CreateScreen(ScreenWidget):
    def __init__(self):
        super().__init__()
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
        self.layout.addWidget(title_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.priority_label)
        self.layout.addWidget(priority_widget)
        self.layout.addWidget(add_todo_button)
        self.layout.addWidget(output_label)
        self.layout.addWidget(self.todo_container)

        # [OPTIONAL] Add a stretch to move everything up
        self.layout.addStretch()

    
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
