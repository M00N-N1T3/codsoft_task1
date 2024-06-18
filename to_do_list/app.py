from lib import click
from logic import logic


PR_PROMPT = str(logic.PRIORITIES.values()).strip("dict_values()")

@click.group()
def main():
    pass


@main.command(help ="Add a new task to your todo-list")
@click.option("-n","--name",prompt = "Enter task name.", help = "task name")
@click.option("-d","--description", prompt ="Enter task description.",help = "task description")
@click.option("-p","--priority", prompt ="Enter task priority " + PR_PROMPT,help = "task priority")
@click.option("-f","--file-name",default = "",help = "to-do_list filename")
def add(name,description,priority,file_name):

    print(name)
    if file_name == "":
        click.echo("works")

    pass

@main.command()
def update():
    pass

@main.command()
def delete():
    pass

@main.command()
def view():
    pass

@main.command()
def status():
    pass


if __name__ == "__main__":
    main()



