"""
Handles the main logic for operating with / writing on to our todo list
"""
from os.path import basename
from os import get_terminal_size
# from lib.tabulate import tabulate

PRIORITIES = {
    "O" : "OPTIONAL",
    "L" : "LOW",
    "M" : "MEDIUM",
    "H" : "HIGH",
    "U" : "URGENT"
}

STATUS = {
    "N" : "NOT STARTED", # \u2610
    "I" : "IN PROGRESS", # \u25CB
    "C" : "COMPLETED" # u'\u2713'
}

DEFAULT_FILENAME = "todo_list.txt"
DEFAULT_TRIGGER = "ALL"
DEFAULT_STATE = "NOT STARTED"


def add_task(task_name: str, description: str, priority:str, file_name = DEFAULT_FILENAME,status = DEFAULT_STATE):
    """
    Adds a new task to the todo list

    Args:
        dir (str): save path of the todo list [DEFAULT = todo_list.txt]
        task_name (str): the name of task
        description (str): a small description regarding the task
        priority (str): PRIORITY of the task

    Returns:
        message : success message
    """

    tasks = []

    try:
        # first we try to read the data on the file
        with open(file_name,"r") as file:
            tasks = file.readlines() # creating a list of all the available files
    except (FileNotFoundError):
        pass

    priority = get_dict_value(PRIORITIES,priority.upper())
    task = f'"{len(tasks)+1}" "{priority}" "{task_name}" "{description}" "{status}"'

    # appending new task to list of current tasks
    if len(tasks) >= 1 and not "\n" in tasks[len(tasks)-1][-1]: # [-1] indicates last element
        tasks.append(f'\n{task}')
    else:
        tasks.append(task)


    # overwriting the file with new data
    try :
        with open(file_name,"w") as file:
            file.writelines(tasks)
            file.close()
        return f"Successful added {task_name} to {basename(file_name)}"
    except Exception as e:
        return f"Successful added {task_name} to {basename(file_name)}"

def view_task(trigger = DEFAULT_TRIGGER ,file_name = DEFAULT_FILENAME,):
    """
    Displays all the tasks on your todo list.

    Args:
        trigger (str, optional) : Trigger flag , triggers an output for only the requested task of Priority n.
        dir (str, optional): The directory of the file. Defaults to DEFAULT_NAME (todo_list.txt).
    """
    tasks = read_file(file_name)
    if len(tasks) < 1:
        result = tabulate([["You have no tasks."]],tablefmt="fancy_grid")
        # print(result)
        return

    for key, value in PRIORITIES.items():

        if trigger == DEFAULT_TRIGGER:
            break

        # if the trigger word is the same as any of values we break
        if trigger == value:
            break

        # in the event of an abbreviated trigger we use the key to get full trigger
        if trigger == key:
            trigger = value
            break

    # for task in enumerate(tasks):

    #     if f'{HEADER}\n' in task or task[1].strip() == HEADER:
    #         print(tabulate('[#] ',task[1].strip()))
    #     else:

    #         # prints everything in the list
    #         if trigger == DEFAULT_TRIGGER:
    #             print(f'[{task[0]}]',"",task[1], end="")

    #         # prints only requested data
    #         elif trigger in task[1]:
    #             print(f'[{task[0]}]',"",task[1], end="")

    #     if "\n" in task[1] and trigger in task:
    #         print()
    #     elif "\n" not in task[1] and trigger == DEFAULT_TRIGGER:
    #         print()

    # for task in tasks:

    try:
        terminal_size = get_terminal_size() + 10
    except Exception as e:
        terminal_size = 50

    headers = ["ID","PRIORITY","NAME","DESCRIPTION"]
    data = [task.strip().split(" ") for task in tasks if trigger]

    requested_data = []
    for task in data:
        if trigger == "ALL":
            requested_data.append(task)
        else:
            if trigger in task:
                requested_data.append(task)

    print(tabulate(requested_data,headers=headers,tablefmt="fancy_grid",maxcolwidths=terminal_size))




def delete_task(index, file_name = DEFAULT_FILENAME):
    """_summary_

    Args:
        index (_type_): _description_
        file_name (_type_, optional): _description_. Defaults to DEFAULT_FILENAME.

    Returns:
        _type_: _description_
    """
    tasks = read_file(file_name)
    if index > len(tasks)-1:
        return 'Selected task number does not exists.'


    # confirm deleting
    choice = input(f"Confirm delete of task (y/yes): ").lower()

    if choice == 'y' or choice == 'yes':
        # deleting task
        del tasks[index]

        # stripping the newline character from the last entry in the list
        tasks[len(tasks)-1] = tasks[len(tasks)-1].strip()

        # overwriting the file with new data
        with open(file_name,"w") as file:
            file.writelines(tasks)
            file.close()

        return f"Successful deleted task {index} from {basename(file_name)}"
    else:
        return f"Aborting operation."


def update_task(task_data : list ,new_task_data:list, file_name = DEFAULT_FILENAME):
    """
    Updates an existing task within our todo_list file

    Args:
        task_data (list): the data and index to update
        new_task_data (list): the data to inject
        file_name (str, optional): todo_list file name if specified [Default = todo_list.txt]

    Returns:
        str: result message
    """
    write = False
    index, tasks = task_data

    old_task_data = task_properties(tasks[index])

    new_task = modify_task(old_task_data,new_task_data)

    tasks[index] = new_task if index == len(tasks)-1 else f"{new_task}\n"

    # overwriting the file with new data
    try:
        with open(file_name,"w") as file:
            file.writelines(tasks)
            file.close()
        write = True
    except Exception as e:
        pass

    return write



def task_properties(task: str):
    """
    generates a list entity of the task

    Args:
        task (str): the task we need to break apart
    Return:
        list :
    """

    task_data = task.split(" ")

    task_id = task_data[0]
    task_state = task_data[1]
    task_priority = task_data[2]
    task_name  = task_data[3]
    task_description  = task_data[4]

    return [task_id,task_priority, task_state, task_name, task_description]



def modify_task(original_task_data: list, new_task_data: tuple):

    priority , task_name, description = new_task_data

    # priority only
    if task_name == "" and description == "" and priority != "":
        original_task_data[1] = priority

    # name only
    elif task_name != "" and description == "" and priority == "":
        original_task_data[2] = task_name

    # description
    elif task_name == "" and description != "" and priority == "":
        original_task_data[3] = description

    # name and description
    elif task_name != "" and description != "" and priority == "":
        original_task_data[2] = task_name
        original_task_data[3] = description

    # name and priority
    elif task_name != "" and description == "" and priority != "":
        original_task_data[2] = task_name
        original_task_data[1] = priority

    # priority and description
    elif task_name == "" and description != "" and priority != "":
        original_task_data[1] = priority
        original_task_data[3] = description

    # everything
    else:
        original_task_data[1] = priority
        original_task_data[2] = task_name
        original_task_data[3] = description

    return f'{original_task_data[0]} "{original_task_data[1]}" "{original_task_data[2]}" "{original_task_data[3]}" "{original_task_data[4]}"'



def modify_status(task_properties: list, status: str):
    status = get_dict_value(STATUS,status.upper().strip())
    
    if status == None:
        exit("Incorrect status. \nAborting operation.")
    return f"[{status}] [{task_properties[1]}] - {task_properties[2]}: {task_properties[3]}"


def change_status(index,status,file_name=DEFAULT_FILENAME):
    """
    Change the status of a task

    Args:
        index (int): the index of the task we want to modify
        file_name (str, optional): The name of the file we want to modify. Defaults to DEFAULT_FILENAME.

    Returns:
        _type_: _description_
    """

    tasks = read_file(file_name)

    if index > len(tasks)-1:
        return 'Selected task number does not exists.'

    data = task_properties(tasks[index])
    new_task_data = modify_status(data,status)
    tasks[index] = new_task_data if index == len(tasks)-1 else f"{new_task_data}\n"
    
    with open(file_name,"w") as file:
        file.writelines(tasks)
        file.close()
    print(f"\nSuccessfully updated task {index}.")



def get_dict_value(dic: dict, given_key:str):
    for key, value in dic.items():
        if key == given_key:
            return value

        if value == given_key:
            return value

def read_file(filename: str= DEFAULT_FILENAME):
    tasks = []
    try:
        with open(filename) as file:
            tasks = file.readlines()
    except (FileNotFoundError):
        exit("Todo list does not exist: {}".format(DEFAULT_FILENAME))

    return tasks