from lib import click
from logic import logic
from logic.os_mod import DOWNLOADS, CWD, HOME,join


PR_PROMPT = str(logic.PRIORITIES.values()).strip("dict_values()")
CONFIG_DIR = join(HOME,"betterMe")


@click.group()
def main():
    return


@main.command(help ="Add a new task to your todo-list")
@click.option("-n","--name",prompt = "Enter task name", required = True,help = "task name")
@click.option("-d","--description", prompt ="Enter task description",help = "task description")
@click.option("-p","--priority", prompt ="Enter task priority" + PR_PROMPT,help = "task priority")
@click.option("-f","--file-name",default = "",help = "to-do_list filename")
def add(name,description,priority,file_name):

    if file_name == "":
        user_input = input(f"Enter file in which to save the todo list ({logic.DEFAULT_FILENAME}): ")
        if user_input == "":
            file_name = logic.DEFAULT_FILENAME
        else:
            file_name = f"{user_input}.txt" if ".txt" not in user_input else user_input

    logic.add_task(name,description,priority,file_name)
    return


@main.command(help="update an existing task.")
@click.option("-i","--index",type=int,prompt = "Enter the task number",help="the index of the task you want to update")
@click.option("-n","--name",help="the new name if you wish to update the name of the task",default = "")
@click.option("-d","--description",help = "the new description for the task if you wish to change the task description",default="")
@click.option("-p","--priority",help=f"the new priority if you wish to update the task priority {PR_PROMPT}",default="")
@click.option("-f","--filename",default ="",help="the absolute path + filename of your todo list file")
def update(index,name,description,priority,filename):

    if filename == "":
        filename = "/home/void/Desktop/project_space/CODSOFT/to_do_list/todo_list.txt"


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



@main.command(help = "delete an existing task")
@click.option("-i","--index",type=int,prompt = "Enter the task number",help="the index of the task you want to update")
@click.option("-f","--filename",default ="",help="the absolute path + filename of your todo list file")
def delete(index,file_name):

    if filename == "":
        filename = "/home/void/Desktop/project_space/CODSOFT/to_do_list/todo_list.txt"

    message = logic.delete_task(index,file_name)
    print(message)

    return



@main.command(help="displays your tasks")
@click.option("-f","--filter",help="filter to display certain tasks based off of their priority",default = "ALL")
@click.option("-p","--path",help="the path of your todo_list file",default="")
def view(filter,path):

    if path == "":
        path = "/home/void/Desktop/project_space/CODSOFT/to_do_list/todo_list.txt"

    logic.view_task(filter.upper(),path)


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


@main.command(help = "change the status of a task")
@click.option("-i","--index",type=int,prompt = "Enter the task number",help="the index of the task you want to update")
@click.option("-s","--status",prompt = "Enter the new status ",help="change progress of task [NOT STARTED, IN PROGRESS, COMPLETED]")
def status():
    pass

"""TODO: a setup that checks for a config. the config stores all the available todo list paths"""
"""TODO: learn tabulate for viewing"""
"""TODO: test the status update, create a new todo list"""

if __name__ == "__main__":
    # print(logic.PRIORITIES.values())
    # print(PR_PROMPT)
    main()
    path = "/home/void/Desktop/project_space/CODSOFT/to_do_list/todo_list.txt"
    # logic.view_task("L",path)
    # update_menu()
    # logic.update_task(1,("p","test1","test"),path)
    # add()
    
    pass




