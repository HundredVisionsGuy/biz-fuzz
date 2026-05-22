"""
controller.py
by Chris Winikka
Deals with storing and retrieving data as well as processing and formatting
of output for the UI.
"""

# any imports?

# any project-level variables

# functions
def store_data(filename: str, data: str) -> bool:
    """stores data to file and returns if it was successful"""
    file_path = "data/" + filename
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
    
if __name__ == "__main__":
    get_file_result = get_data("hello.txt")
    print(get_file_result)
    success = store_data("hello.txt", "Hi there!")
    if success:
        print("Huzzah!")
    else:
        print("DOH!")
