from os import path

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
HEADER = "[STATUS] [PRIORITY] - NAME: DESCRIPTION"

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

    priority = get_dict_value(PRIORITIES,priority.upper())
    string = f"[{priority}] [{status}] - {task_name}: {description}"
    tmp = string.split('-')
    name = tmp[1].split(':')[0].strip()

    try:
        # first we try to read the data on the file
        with open(file_name,"r") as file:
            tasks = file.readlines() # creating a list of all the available files
    except (FileNotFoundError):
        pass

    # ensuring that the file will always have a Header
    if len(tasks) <= 0 or tasks[0].strip() != HEADER:
        tasks.insert(0,HEADER)

    # appending new task to list of current tasks
    tasks.append(f'\n{string}')

    # overwriting the file with new data
    with open(file_name,"w") as file:
        file.writelines(tasks)
        file.close()

    if (status != DEFAULT_STATE):
        return f"Successful added {name}. STATUS ({status})"

    return f"Successful added {task_name}."

def view_task(trigger = DEFAULT_TRIGGER ,file_name = DEFAULT_FILENAME,):
    """
    Displays all the tasks on your todo list.

    Args:
        trigger (str, optional) : Trigger flag , triggers an output for only the requested task of Priority n.
        dir (str, optional): The directory of the file. Defaults to DEFAULT_NAME (todo_list.txt).
    """

    tasks = []

    try:
        with open(file_name) as file:
            tasks = file.readlines()
    except (FileNotFoundError):
        return "Todo list does not exist"

    if len(tasks) < 1:
        print("You have no tasks.")

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

    for task in enumerate(tasks):

        if f'{HEADER}\n' in task or task[1].strip() == HEADER:
            print('[#] ',task[1].strip())
        else:

            # prints everything in the list
            if trigger == DEFAULT_TRIGGER:
                print(f'[{task[0]}]',"",task[1], end="")

            # prints only requested data
            elif trigger in task[1]:
                print(f'[{task[0]}]',"",task[1], end="")

        if "\n" in task[1] and trigger in task:
            print()
        elif "\n" not in task[1] and trigger == DEFAULT_TRIGGER:
            print()



def delete_task(index, file_name = DEFAULT_FILENAME):

    tasks = []
    tmp = []

    try:
        with open(DEFAULT_FILENAME,'r') as file:
            tasks = file.readlines()
            file.close()
    except (FileNotFoundError):
        return "Todo list does not exist"


    if index > len(tasks)-1:
        return 'Selected task number does not exists.'


    # getting task name
    tmp = tasks[index].split('-')[1]
    task_name = tmp.split(':')[0].strip()

    # confirm deleting
    choice = input(f"Confirm delete of task {tasks[index]} (y/yes): ").lower()

    if choice == 'y' or choice == 'yes':
        # deleting task
        del tasks[index]

        # stripping the newline character from the last entry in the list
        tasks[len(tasks)-1] = tasks[len(tasks)-1].strip()

        # overwriting the file with new data
        with open(file_name,"w") as file:
            file.writelines(tasks)
            file.close()

        return f"Successful deleted {task_name} from tasks!"
    else:
        return f"Aborting deleting of {task_name}"


def update_task(index : int,new_task_data:list, file_name = DEFAULT_FILENAME):

    tasks = []
    # priority,task_name,description = new_task_data


    try:
        with open(file_name,'r') as file:
            tasks = file.readlines()
            file.close()
    except (FileNotFoundError):
        print("Todo list does not exist")
        return

    if index > len(tasks)-1:
        print('Selected task number does not exists.')
        return

    print(f'Selected task: {tasks[index].strip()}')

    old_task_data = task_properties(tasks[index])

    new_task = modify_task(old_task_data,new_task_data)

    """TODO: WRITE the data"""
    print(f"Successfully updated task {index}.")

    return new_task



def task_properties(task: str):
    """
    generates a list entity of the task

    Args:
        task (str): the task we need to break apart
    Return:
        list :
    """

    task_data = task.split("-")[0].strip()

    # [Complete]
    task_state = task_data.split("]")[0].replace("[","").replace("]","").strip()
    # [urgent]
    task_priority = task_data.split("]")[1].replace("[","").replace("]","").strip()

    task_name  = task.split("-")[1].split(":")[0].strip()
    task_description  = task.split("-")[1].split(":")[1].strip()

    return [task_state, task_priority, task_name, task_description]



def modify_task(original_task_data: list, new_task_data: tuple):

    task_name, description, priority = new_task_data

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

    return f"[{original_task_data[0]}] [{original_task_data[1]}] - {original_task_data[2]}: {original_task_data[3]}"



def modify_status(task_properties: list, status: str):

    status = get_dict_value(status)

    return f"[{status}] [{task_properties[1]}] - {task_properties[2]}: {task_properties[3]}"


def change_status(index,file_name=DEFAULT_FILENAME):

    tasks = []
    try:
        with open(file_name,'r') as file:
            tasks = file.readlines()
            file.close()
    except (FileNotFoundError):
        return "Todo list does not exist"


    if index > len(tasks)-1:
        return 'Selected task number does not exists.'

    data = task_properties(tasks[index])
    new_data = modify_status(data,)
    tasks[index] = new_data



def get_dict_value(dic: dict, given_key:str):
    for key, value in dic.items():
        if key == given_key:
            return value


        if value == given_key:
            return value


