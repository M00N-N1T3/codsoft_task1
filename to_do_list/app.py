from lib import click
from logic import logic
from logic.os_mod import DOWNLOADS, CWD, HOME


PR_PROMPT = str(logic.PRIORITIES.values()).strip("dict_values()")
@click.group()
def main():
    pass


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


@main.command()
def update():

    pass

@main.command()
def delete():
    pass



@main.command(help="displays your tasks")
@click.option("-f","--filter",help="filter to display certain tasks based off of their priority",default = "ALL")
@click.option("-p","--path",help="the path of your todo_list file",default="")
def view(filter,path):

    if path == "":
        path = "/home/void/Desktop/project_space/CODSOFT/to_do_list/todo_list.txt"

    logic.view_task(filter.upper(),path)


@main.command()
def status():
    pass


if __name__ == "__main__":
    # print(logic.PRIORITIES.values())
    # print(PR_PROMPT)
    # main()
    path = "/home/void/Desktop/project_space/CODSOFT/to_do_list/todo_list.txt"
    logic.view_task("L",path)
    # add()
    pass




