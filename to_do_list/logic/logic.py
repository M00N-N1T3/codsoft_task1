from os import path

PRIORITIES = {
    "o" : "Optional",
    "l" : "Low",
    "m" : "Medium",
    "h" : "High",
    "u" : "Urgent"
}

DEFAULT_NAME = "todo_list.txt"
DEFAULT_TRIGGER = "A"
HEADER = "[PRIORITY] - NAME: DESCRIPTION"

def add(name: str, description: str, mode:str, file_name = DEFAULT_NAME):
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


    tasks = []
    string = f"[{mode}] - {name}: {description}"

    tmp = string.split('-')
    task_mode = tmp[0].strip()
    task_name = tmp[1].split(':')[0].strip()

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

    return f"Successful added {task_name} to {task_mode}"


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
    print()

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




import random
choices = ["crucial","low","high"]
# for i in range (1,10):
#     choice = random.choice(choices)
#     message = add(f"test_{i}","works",choice)
#     print(message)

m = delete_task(1)
print(m)
view_task()