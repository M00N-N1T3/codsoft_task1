from lib import click
from logic import logic
from logic.os_mod import DOWNLOADS, CWD, HOME,join, basename, exists, isfile, remove, listdir


def main_path():
    return join(DOWNLOADS,"TaskIT")

def file_path(file):
    file = f"{file}.txt" if not ".txt" in file else file
    return join(DOWNLOADS,"TaskIT",file)
    

PR_PROMPT = str(logic.PRIORITIES.values()).strip("dict_values()")
STATUS_PROMPT = str(logic.STATUS.values()).strip("dict_values()")
CONFIG_DIR = join(HOME,"betterMe")
MAIN_PATH = main_path()

@click.group()
def main():
    return

# completed
@main.command(help ="Add a new task to your todo-list")
@click.option("-n","--name",prompt = "Enter task name", required = True,help = "task name")
@click.option("-d","--description", prompt ="Enter task description",help = "task description")
@click.option("-p","--priority", prompt ="Enter task priority" + PR_PROMPT,help = "task priority")
@click.option("-f","--file-name",default = "",help = "to-do_list filename")
def add_task(name,description,priority,file_name):

    if file_name == "":
        user_input = input(f"Enter file in which to save the todo list ({logic.DEFAULT_FILENAME}): ")
        if user_input == "":
            file_name = file_path(logic.DEFAULT_FILENAME)
        else:
            file_name = file_path(user_input)

    logic.add_task(name,description,priority,file_name)
    return


# completed
@main.command(help="update an existing task.")
@click.option("-i","--index",type=int,prompt = "Enter the task number",help="the index of the task you want to update")
@click.option("-n","--name",help="the new name if you wish to update the name of the task",default = "")
@click.option("-d","--description",help = "the new description for the task if you wish to change the task description",default="")
@click.option("-p","--priority",help=f"the new priority if you wish to update the task priority {PR_PROMPT}",default="")
@click.option("-f","--filename",prompt = f"Enter the name of the file",default =logic.DEFAULT_FILENAME,help="the absolute path + filename of your todo list file")
def update_task(index,name,description,priority,filename):

    filename = file_path(filename)
    tasks = logic.read_file(filename)
    print(f"Selected task: {tasks[index]}")

    if name == "" and description == "" and priority =="":
        new_task_data = update_menu()
        if new_task_data == ("","",""):
            print("Aborting operation...")
            return
    else:
        new_task_data = [name,description,priority.upper()]

    if new_task_data[2] != "":
        if new_task_data[2].upper() in logic.PRIORITIES.keys():
            new_task_data[2] = logic.PRIORITIES.get(new_task_data[2])
        elif new_task_data[2].upper() in logic.PRIORITIES.values():
            pass
        else:
            print(f"You have chosen an invalid priority {new_task_data[2]}")
            print(f"These are the available priorities {PR_PROMPT}")
            return

    logic.update_task(index,new_task_data,filename)
    return


# in progress
@main.command(help = "delete an existing task")
@click.option("-i","--index",type=int,prompt = "Enter the task number",help="the index of the task you want to update")
@click.option("-f","--filename",default =logic.DEFAULT_FILENAME,help="the name of the todo list file")
def delete_task(index,filename):
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
    files = listdir(MAIN_PATH)
    if len(files) < 1:
        print("You currently own no todo_list files")
        return
    else:
        print("Your available todo_list files: ")
        
    for file in  files:
        print(file)
        

# helpers
def update_menu():
    """
    task update controller. Only triggers if user does not specify what they want to
    change via flags

    Returns:
        tuple : (str,str,str)
    """

    print('''1) Change priority.
2) Change task name.
3) Change description.
4) Change all.
0) Cancel\n''')

    breaker = 0

    while True:
        choice = input('Select only one of the above options: ').lower().strip()

        if breaker > 2 or choice == "0":
            if choice != "0":
                print('To many incorrect entires.')
            return "","",""

        if choice == "1":
            priority = input(f"Enter new priority [{PR_PROMPT}]: ")
            return ["","",priority]
        elif choice == "2":
            name = input(f"Enter the new task name: ")
            return [name,"",""]
        elif choice == "3":
            desc= input("Enter the new task description: ")
            return ["",desc,""]
        elif choice == "4":
            priority = input(f"Enter new priority [{PR_PROMPT}]: ")
            name = input(f"Enter the new task name: ")
            desc= input("Enter the new task description: ")
            return [name,desc,priority]

        breaker +=1
        


"""TODO: a setup that checks for a config. the config stores all the available todo list paths"""
"""TODO: learn tabulate for viewing"""
"""TODO: test the status update, create a new todo list"""
"""TODO: Add a logic for length less than 5 then do not write it"""
if __name__ == "__main__":
    # print(logic.PRIORITIES.values())
    # print(PR_PROMPT)
    main()
    # add_task()
    # path = "/home/wtc/Desktop/project_space/CODSOFT/to_do_list/todo_list.txt"
    # logic.view_task("L",path)
    # update_menu()
    # logic.update_task(1,("p","test1","test"),path)
    # add()
    # update_task()
    
    pass




