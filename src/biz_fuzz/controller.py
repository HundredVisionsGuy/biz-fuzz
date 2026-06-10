"""
controller.py
by Chris Winikka
Deals with storing and retrieving data as well as processing and formatting
of output for the UI.
"""

# any imports?
import os

# any project-level variables
data_path = "data/"
todo_list_path = "data/todo_lists/"


# functions
def store_data(filename: str, data: str, dir="data/todo_lists/") -> bool:
    """stores data to file and returns if it was successful"""
    file_path = dir + filename
    try:
        with open(file_path, 'w') as f:
            f.write(data)
    except Exception as e:
        print("Oops! something went wrong")
        print(str(e))
        return False
    return True


def get_data(filename: str) -> str:
    """gets data from file"""
    file_path = "data/" + filename
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            return data
    except FileNotFoundError:
        error = "ERROR that file does not exist"
        return error


def get_todo_lists() -> list:
    """Get all filenames from todo_list folder
    
    todo_list_path is the folder where all the json files
    of todo lists reside.

    Returns:
        file_list: a list of filenames from folder
    """
    file_list = []
    with os.scandir(todo_list_path) as files:
        for file in files:
            if file.is_file():
                file_list.append(file.name)
    return file_list


if __name__ == "__main__":
    get_file_result = get_data("hello.txt")
    print(get_file_result)
    success = store_data("hello.txt", "Hi there!")
    if success:
        print("Huzzah!")
    else:
        print("DOH!")
