"""
create_screen.py
by HundredVisionsGuy
A base class for each screen in the stacked layout
"""
import controller
import json

from PySide6.QtWidgets import (
    QButtonGroup,
    QCheckBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget)
from screen_widget import ScreenWidget

class CreateScreen(ScreenWidget):
    def __init__(self):
        super().__init__()
        self.title_label.setText("Create a Todo list.")

        # Widgets to create a Todo Item
        # Todo List Name
        todo_name_layout = QHBoxLayout()
        todo_name_label = QLabel("Name Your ToDO List:")
        self.todo_name_input = QLineEdit()
        self.todo_name_input.setPlaceholderText("Todo List Name")
        todo_name_layout.addWidget(todo_name_label)
        todo_name_layout.addWidget(self.todo_name_input)

        # Todo Item Description
        item_description_layout = QHBoxLayout()
        item_description_label = QLabel("Your Todo Description: ")
        self.todo_description_input = QLineEdit()
        self.todo_description_input.setPlaceholderText("What do you want to do?")
        item_description_layout.addWidget(item_description_label)
        item_description_layout.addWidget(self.todo_description_input)

        # Todo Priority
        self.priority_label = QLabel("Set Priority Level ")

        # NOTE: a QButtonGroup is not a widget
        self.priority_group = QButtonGroup()
        self.priority_group.setExclusive(True)

        # We have to set a widget for the QButtonGroup
        priority_widget = QWidget()
        priority_layout = QHBoxLayout()

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

        # Save / Clear List
        save_clear_layout = QHBoxLayout()
        save_list_button = QPushButton("Save")
        save_list_button.clicked.connect(self.save_list)

        clear_list_button = QPushButton("Clear")
        clear_list_button.clicked.connect(self.clear_list)
        save_clear_layout.addWidget(save_list_button)
        save_clear_layout.addWidget(clear_list_button)

        # add widgets & layouts to main layout
        self.layout.addLayout(todo_name_layout)
        self.layout.addLayout(item_description_layout)
        self.layout.addWidget(self.priority_label)
        self.layout.addWidget(priority_widget)
        self.layout.addWidget(add_todo_button)
        self.layout.addWidget(output_label)
        self.layout.addWidget(self.todo_container)
        self.layout.addLayout(save_clear_layout)

        # [OPTIONAL] Add a stretch to move everything up
        self.layout.addStretch()

    
    def add_todo_item(self):
        todo_name = self.todo_description_input.text()
        self.todo_description_input.setText("")

        checked_priority = self.priority_group.checkedButton()
        todo_priority = checked_priority.text()
        checked_priority.setChecked(False)

        todo_string = f"{todo_name} -> {todo_priority}"
        todo_button = QCheckBox(todo_string)
        self.todo_list.addButton(todo_button)
        self.todo_layout.addWidget(todo_button)

    def save_list(self):
        # Get data from list
        list_title = self.todo_name_input.text()
        todo_dict = {
            "title": list_title,
            "items": []
        }

        todo_btns = self.todo_list.buttons()
        todo_list = []
        for btn in todo_btns:
            text = btn.text()
            todo_item = text.split(" -> ")
            todo = {"description": todo_item[0],
                    "priority": todo_item[1]}
            todo_list.append(todo)

        # Store as a dictionary
        list_title += ".json"
        list_title = "todo_lists/" + list_title
        todo_dict["items"] = todo_list
        todo_json = json.dumps(todo_dict)

        # Save it to data folder
        success = controller.store_data(list_title, todo_json)

        # Clear List
        if success:
            self.clear_list()

        print("ERROR")

    def clear_list(self):
        pass