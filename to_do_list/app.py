from lib import click, tabulate
from logic import logic
from logic.os_mod import DOWNLOADS, CWD, HOME,join, basename, exists, isfile, remove, listdir, mkdir


def main_path():
    return join(DOWNLOADS,"TaskIT")

def file_path(file):
    file = f"{file}.txt" if not ".txt" in file else file
    return join(DOWNLOADS,"TaskIT",file)


PR_PROMPT = str(logic.PRIORITIES.values()).strip("dict_values()")
STATUS_PROMPT = str(logic.STATUS.values()).strip("dict_values()")
CONFIG_DIR = join(HOME,"betterMe")
MAIN_PATH = main_path()
clear_term ="\033c"


@click.group()
def main():
    return

# completed
@main.command(help ="Add a new task to your todo-list")
@click.option("-n","--name",prompt = "Enter task name", required = True,help = "task name")
@click.option("-d","--description", prompt ="Enter task description",help = "task description")
@click.option("-p","--priority", prompt ="Enter task priority" + PR_PROMPT,help = "task priority")
@click.option("-f","--file-name",default = "",help = "to-do_list filename")
def add_task(name: str,description:str ,priority: str, file_name:str ):
    """
    Adds a new task to our todo list
    Args:
        name (str):the task name
        description (str):task description
        priority (str): the priority of the task
        file_name (str, optional): todo_list file name if specified [Default = todo_list.txt]
    """

    if file_name == "":
        user_input = input(f"Enter file in which to save the todo list ({logic.DEFAULT_FILENAME}): ")
        if user_input == "":
            file_name = file_path(logic.DEFAULT_FILENAME)
        else:
            file_name = file_path(user_input)

    result = logic.add_task(name,description,priority,file_name)
    tab = tabulate.tabulate([[result]],tablefmt="fancy_grid")
    print(clear_term, end=tab+"\n")
    return



@main.command(help="update an existing task.")
@click.option("-i","--index",type=int,prompt = "Enter the task number",help="the index of the task you want to update")
@click.option("-n","--name",help="the new name if you wish to update the name of the task",default = "")
@click.option("-d","--description",help = "the new description for the task if you wish to change the task description",default="")
@click.option("-p","--priority",help=f"the new priority if you wish to update the task priority {PR_PROMPT}",default="")
@click.option("-f","--filename",prompt = f"Enter the name of the file",default =logic.DEFAULT_FILENAME,help="the absolute path + filename of your todo list file")
def update_task(index: int, name: str, description: str, priority: str ,filename: str):
    """
    Updates an existing task
    Args:
        index (int): the index to update
        name (str):the task name
        description (str):task description
        priority (str): the priority of the task
        file_name (str, optional): todo_list file name if specified [Default = todo_list.txt]
    """

    filename = file_path(filename)
    tasks = logic.read_file(filename)
    updating_data = ""


    if index == 0 or index > len(tasks)-1:
        tab = tabulate.tabulate([['The selected task number does not exists.']],tablefmt="fancy_grid")
        print(tab)
        return

    # index correction so that we can retrieve correct data
    index -=1
    if name == "" and description == "" and priority =="":
        new_task_data, message = update_menu()
        if new_task_data == ["","",""]:
            tab = tabulate.tabulate([[f"{message} \nAborting operation..."]],tablefmt="fancy_grid")
            print(clear_term, end=tab+"\n")
            return
    else:
        # new_task_data, updating_data = [priority.upper(),name,description,]
        new_task_data = [priority.upper(),name,description,]

    # the priority selected by the user
    if new_task_data[0] != "":
        if new_task_data[0] in logic.PRIORITIES.keys():
            new_task_data[0] = logic.PRIORITIES.get(new_task_data[0])
        elif new_task_data[0] in logic.PRIORITIES.values():
            pass
        else:
            m1 = f"You have chosen an invalid priority {new_task_data[2]}"
            m2 = f" \nThese are the available priorities {PR_PROMPT}"
            tab = tabulate.tabulate([[m1 + m2]],tablefmt="fancy_grid")
            print(clear_term, end=tab+"\n")
            return


    selected_task = f"Selected task {tasks[index].split(" ")[0].strip('\" \"')}: {tasks[index].split(" ")[3].strip(" ")}"

    result = logic.update_task([index,tasks],new_task_data,filename)
    message = update_message(new_task_data)

    result_message = "Successfully" if result else "Failed to"
    message = f"{result_message} updated the {message} of task {tasks[index].split(" ")[0].strip('\" \"')}."

    print()
    tab = tabulate.tabulate([["{} \n{}".format(selected_task,message)]],tablefmt="fancy_grid")
    print(end=tab+"\n")




# in progress
@main.command(help = "delete an existing task")
@click.option("-i","--index",type=int,prompt = "Enter the task number",help="the index of the task you want to update")
@click.option("-f","--filename",default =logic.DEFAULT_FILENAME,help="the name of the todo list file")
def delete_task(index,filename):
    """
    Deletes an existing task form our todo_list file

    Args:
        index (int): _description_
        filename (_type_): _description_
    """
    filename = file_path(filename)
    tasks = logic.read_file(filename)
    print(f"Selected task: {tasks[index]}",end="")
    message = logic.delete_task(index,filename)
    print(message)
    return



@main.command(help="displays tasks from a selected todo_list")
@click.option("-f","--filter",help="filter to display certain tasks based off of their priority",default = "ALL")
@click.option("-p","--path",help="the filename of the todo_list file if not specified",default=logic.DEFAULT_FILENAME)
def view_tasks(filter,path):
    path = file_path(path)
    logic.view_task(filter.upper(),path)



@main.command(help = "change the status of a task")
@click.option("-i","--index",type=int,required=1,prompt = "Enter the task number",help="the index of the task you want to update")
@click.option("-s","--status",prompt = f"Select a new status {STATUS_PROMPT}",help="change progress of task [NOT STARTED, IN PROGRESS, COMPLETED]")
@click.option("-f","--filename",required =1,prompt = f"Enter filename",default =logic.DEFAULT_FILENAME,help="the name of the todo list file")
def change_status(index,status,filename):
    filename = file_path(filename)
    tasks = logic.read_file(filename)
    
    if len(tasks) < 1:
        exit("You have no tasks.")
    
    if index >= len(tasks):
        exit(f"task {index} does not exist in {basename(filename)}")
    
    print(f"Selected task: {tasks[index]}",end="")
    logic.change_status(index,status.upper(),filename)
    return

@main.command(help = "create a new todo_list file")
@click.option("-f","--filename",required=1, prompt = "Enter the name of the file")
def create_file(filename):
    file = file_path(filename)
    if exists(file) and isfile(file):
        choice = input(f"{basename(file)} already exists. Enter yes to overwrite file: ").lower()
        if choice in ["yes","y"]:
            with open(file,"w") as f:
                f.close()
        else:
            print(f"Could not create {basename(file)}.")
    elif not exists(filename):
        with open(file,"w") as f:
            f.close()
        print(f"{basename(file)} has been created")
    else:
        print(f"Error could not create {basename(file)}")
    
        return

@main.command(help="delete an existing task file")
@click.option("-f","--filename",required=1, prompt = "Enter the name of the file")
def delete_file(filename):
    files = listdir(MAIN_PATH)
    filename = file_path(filename)
    choice = ""
    

    if basename(filename) in files:
        choice = input("Confirm (yes/no): ").lower().strip()
    else:
        print(f"{filename} does not exist.")
        return
    
    if choice in ["yes","y"] and exists(filename) and isfile(filename):
        remove(file_path(filename))
        print(f"{basename(filename)} deleted!")
    else:
        if not isfile(filename):
            print(f"{filename} is a dir.")
        print(f"Aborting operation...")
    
    return

@main.command(help="list all available todo lists")
def list_all():
    """
    Lists all the available todo list files in your Downloads/TaskIT folder
    """

    files = listdir(MAIN_PATH)
    clean_data = [file for file in files if ".txt" in file]

    if len(clean_data) < 1:
        tab = tabulate.tabulate(["You currently do not have any todo_lists"],tablefmt="fancy_grid")
        print(tab)
        return

    # creating a numbering system
    todo_list_files = [[clean_data.index(file)+1 ,file] for file in clean_data]

    # tabulating data
    tab = tabulate.tabulate(todo_list_files,headers=["","Available Files"],tablefmt="fancy_grid")
    print(tab)

# helpers
def update_menu():
    """
    task update controller. Only triggers if user does not specify what they want to
    change via flags

    Returns:
        tuple : [str,str,str],message
    """


    header = ["","options"]
    tab = tabulate.tabulate([[1,"Change Priority"],[2, "Change task name"],
        [3, "Change description"],[4,"Change all"],
        [0,"Cancel"]],tablefmt="outline",headers=header)

    breaker = 0

    while True:
        print(clear_term)
        print(tab)
        choice = input('Select only one of the above options: ').lower().strip()

        if breaker > 2 or choice == "0":
            message = "Canceled"
            if choice != "0":
                message = "To many attempts"
            return ["","",""], message

        print()
        if choice == "1":
            priority = input(f"Enter new priority {PR_PROMPT}: ")
            return ["","",priority.upper()], "priority"
        elif choice == "2":
            name = input(f"Enter the new task name: ")
            return [name,"",""], ""
        elif choice == "3":
            desc= input("Enter the new task description: ")
            return ["",desc,""], ""
        elif choice == "4":
            priority = input(f"Enter new priority {PR_PROMPT}: ")
            name = input(f"Enter the new task name: ")
            desc= input("Enter the new task description: ")
            return [priority.upper(),name,desc], ""

        breaker +=1

def update_message(updated_data:list ):
    """
    creates a custom message based of what got updated in the task
    """

    priority , name, description = updated_data

    if priority != "" and name == "" and description =="":
        message = "priority"
    elif name != "" and priority == "" and description =="":
        message = "name"
    elif description != "" and name == "" and priority =="":
        message = description
    else:
        message = "name, description and priority"

    return message

"""TODO: learn tabulate for viewing"""

if __name__ == "__main__":

    if not exists(MAIN_PATH):
        mkdir(MAIN_PATH)
    main()
    # update_task(2,"TEST 2","Testing if it will wokr with spaces","U","todo_list")





