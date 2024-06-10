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
HEADER = "[PRIORITY] - NAME: DESCRIPTION\n"

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
    tasks.append(f'{string}\n')

    # overwriting the file with new data
    with open(dir,"w") as file:
        file.writelines(tasks)
        file.close()

    return f"Successful added {task_name} to {task_mode}"


def view_task(trigger = DEFAULT_TRIGGER ,dir = DEFAULT_NAME,):
    """
    Displays all the tasks on your todo list.

    Args:
        trigger (str, optional) : Trigger flag , triggers an output for only the requested task of Priority n.
        dir (str, optional): The directory of the file. Defaults to DEFAULT_NAME (todo_list.txt).
    """

    tasks = []

    try:
        with open(dir) as file:
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

        if HEADER in task:
            print('[#] ',task[1].strip())
        else:

            # prints everything in the list
            if trigger == DEFAULT_TRIGGER:
                print(f'[{task[0]}]',"",task[1], end="")

            # prints only requested data
            elif trigger in task[1]:
                print(f'[{task[0]}]',"",task[1], end="")

def delete_task(index, file = DEFAULT_NAME):

    tasks = []
    try:
        with open(DEFAULT_NAME,'r') as file:
            tasks = file.readlines()
    except (FileNotFoundError):
        return "Todo list does not exist"

    # deleting
    print(tasks)
    del tasks[index]
    print()
    print(tasks)



# import random
# choices = ["crucial","low","high"]
# for i in range (1,10):
#     choice = random.choice(choices)
#     message = add(f"test_{i}","works",choice)
#     print(message)

# delete_task(9)
view_task()