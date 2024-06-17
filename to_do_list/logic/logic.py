from os import path

PRIORITIES = {
    "o" : "Optional",
    "l" : "Low",
    "m" : "Medium",
    "h" : "High",
    "u" : "Urgent"
}

STATUS = {
    "n" : "not started",
    "i" : "in progress",
    "c" : "completed"
}

DEFAULT_NAME = "todo_list.txt"
DEFAULT_TRIGGER = "A"
DEFAULT_STATE = "NOT STARTED"
HEADER = "[STATUS] [PRIORITY] - NAME: DESCRIPTION"

def add_task(task_name: str, description: str, priority:str, file_name = DEFAULT_NAME,status = DEFAULT_STATE):
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
    string = f"[{status}] [{priority}] - {task_name}: {description}"

    tmp = string.split('-')
    task_priority = tmp[0].strip()
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

    return f"Successful added {name}."

def view_task(trigger = DEFAULT_TRIGGER ,file_name = DEFAULT_NAME,):
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

        # if the trigger word is the same as any of values we break
        if trigger.lower() == value.lower():
            break

        # in the event of an abbreviated trigger we use the key to get full trigger
        if trigger.lower() == key:
            trigger = value.lower()
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



def delete_task(index, file_name = DEFAULT_NAME):

    tasks = []
    tmp = []

    try:
        with open(DEFAULT_NAME,'r') as file:
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


def update_task(index,task_name: str, description: str, priority:str, file_name = DEFAULT_NAME):

    tasks = []
    data = (priority,task_name,description)
    option = ""

    try:
        with open(DEFAULT_NAME,'r') as file:
            tasks = file.readlines()
            file.close()
    except (FileNotFoundError):
        return "Todo list does not exist"

    if index > len(tasks)-1:
        return 'Selected task number does not exists.'

    print(f'You have selected task: {tasks[index]}')

    """TODO: separate prompt to accommodate click """

    choices = {'a':'all','p':'priority','d':'description','n':'name'}

    print('''P) Change priority.
D) Change description.
N) Change task name.
A) Change all.\n''')

    breaker = 0
    while True:
        choice = input('Select only one of the above options: ').lower().strip()

        if breaker > 2:
            print('Aborting. To many incorrect entires.')
            break

        if choice in choices.keys():
            option = choices[choice]
            break
        breaker +=1

    task_property = task_properties(tasks[index])

    new_task = generate_task(task_property,data,option)

    print(new_task)

    return task_property


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

def generate_task(task_property: list, original_data: tuple, option: str):

    priority, task_name, description = original_data

    # if option == "status":
    #     task_property[0] = status
    if option == "priority":
        task_property[1] = priority
    elif option == "name":
        task_property[2] = task_name # name
    elif option == "description":
        task_property[3] = description
    else:
        task_property[1] = priority
        task_property[2] = task_name
        task_property[3] = description

    return f"[{task_property[0]}] [{task_property[1]}] - {task_property[2]}: {task_property[3]}"






""" TODO: add update task method, add status (not_started, in progress, completed)"""
def change_status():
    pass


# import random

# for i in range(10):
#     print(add_task(f"task {i+1}",f"testing_{i+1}",random.choice(["Urgent","Low","Medium"])))
# view_task()
update_task(2,"testing the dam thing","","")
