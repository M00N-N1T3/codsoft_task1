from os import path

PRIORITIES = {
    "o" : "Optional",
    "l" : "Low",
    "m" : "Medium",
    "h" : "High",
    "u" : "Urgent"
}

DEFAULT_NAME = "todo_list.txt"

def add(name: str, description: str, mode:str, dir = DEFAULT_NAME):
    """
    Adds a new task to the todo list

    Args:
        dir (str): save path of the todo list [DEFAULT = todo_list.txt]
        name (str): the name of task
        description (str): a small description regarding the task
        mode (str): PRIORITY of the task

    Returns:
        message : success message
    """

    HEADER = "[#] PRIORITY - NAME: DESCRIPTION\n"
    tasks = [HEADER]
    string = f"[{mode}] - {name}: {description}"

    tmp = string.split('-')
    task_mode = tmp[0].strip()
    task_name = tmp[1].split(':')[0].strip()

    try:
        # first we try to read the data on the file
        with open(dir,"r") as file:
            tasks = file.readlines() # creating a list of all the available files

    except (FileNotFoundError):
        pass

    # appending new task to list of current tasks
    tasks.append(f'[{len(tasks)}] {string}\n');

    # overwriting the file with new data
    with open(dir,"w") as file:
        file.writelines(tasks)
        file.close()

    return f"Successful added {task_name} to {task_mode}"

def delete_task(index, file = DEFAULT_NAME):
    
    tasks = []
    try:
        with open(DEFAULT_NAME,'r'):
            

    pass

import random
choices = ["crucial","low","high"]
for i in range (1,10):
    choice = random.choice(choices)
    message = add(f"test_{i}","works",choice)
    print(message)