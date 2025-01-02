FILEPATH="todos_2.txt"

def get_todos(file_path_local=FILEPATH):
    """ Opens the todo file and returns the contents as a list."""
    with open(file_path_local, "r") as file:
        todos_local = file.readlines()
    return todos_local

def save_todos(todos_local, file_path_local=FILEPATH):
    """ Saves the list in the todo text file. Requires argument for current todo list."""
    with open(file_path_local, "w") as file:
        file.writelines(todos_local)

if __name__ == "__main__":
    print(FILEPATH)