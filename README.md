# Projet number 1 from roadmap.sh backend projects

## Rules :

Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

### Requirements :

The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

Add, Update, and Delete tasks
Mark a task as in progress or done
List all tasks
List all tasks that are done
List all tasks that are not done
List all tasks that are in progress
Here are some constraints to guide the implementation:

You can use any programming language to build this project.
Use positional arguments in command line to accept user inputs.
Use a JSON file to store the tasks in the current directory.
The JSON file should be created if it does not exist.
Use the native file system module of your programming language to interact with the JSON file.
Do not use any external libraries or frameworks to build this project.
Ensure to handle errors and edge cases gracefully.

### Task Properties  
Each task should have the following properties:

id: A unique identifier for the task
description: A short description of the task
status: The status of the task (todo, in-progress, done)
createdAt: The date and time when the task was created
updatedAt: The date and time when the task was last updated
Make sure to add these properties to the JSON file when adding a new task and update them when updating a task.

# Solution

## First step 

Try to write on the terminal and read a value write by a user.

Code :

```
print("Hello user, what is your name ?")

name = input()
print("Greatings", name, "!")
```

Outpout :

```
python3 task-tracker.py
Hello user, what is your name ?
Guillaume
Greatings Guillaume !
```

## Second step 

Take the user entry and put the value into a json file.

Code :
```
import json

print("# Adding a new task please")

task = input()

dictionary = {
    "task": task
}

json_object = json.dumps(dictionary, indent=4)

with open("task.json", "w") as outfile:
    outfile.write(json_object)
```

Outpout :

```
{
    "task": "First task"
}
```

### Third step

Create a command line application that will wait for instructions.

```
def main():
    print("Welcome to Task Tracker CLI !\n")
    print("""For beggining write the command add follow 
by your task to add a new task it into our tool.\n
Use the command "help" for the list of available commands.
""")

    while True:
        command = input("=> ")
        if command == "exit":
            print("See you soon !")
            break
        elif command.startswith("add "):
            task = command[4:].strip()             
            addTask(task)
        elif command.startswith("delete "):
            try:
                with open("tasks.json", "r") as infile:
                    tasks = json.load(infile)
                    if tasks:
                        print("Write the id of the task you want delete.")
                        idTask = command[7:].strip()
                        deleteTask(idTask)
                    else:
                        print("You have no task yet, they are nothing to delete")
            except FileNotFoundError:
                print("You have no task yet, they are nothing to delete")
        elif command == "list":
            tasksList()
        elif command.startswith("update "):
            idTask = command[7:8].strip()
            updatedTask = command[8:].strip()
            updateTask(idTask, updatedTask)
        elif command == "help":
            print("""
This are the command availables :
    - add : add your task in our system
    - delete : delete a task by enter is ID
    - exit : terminate the application
    - list : list all your tasks
""")
        else:
            print("Command not found. Use help for a list of command availables.")

if __name__ == "__main__":
    main()
```

### Fourth step

Add a function for write multiple task and a command for listing all the tasks.

```
def addTask(task):
    try:
        with open("tasks.json", "r") as infile:
            tasks = json.load(infile)
    except FileNotFoundError:
        tasks = []

    if len(tasks) == 0:
        id = 1
    else:
        id = tasks[-1]["id"] + 1

    tasks.append({"id": id, "task": task})

    with open("tasks.json", "w") as outfile:
        json.dump(tasks, outfile, indent=4)

    print("# Task added successfully (ID:", id,")")

def tasksList():
    try:
        with open("tasks.json", "r") as infile:
            tasks = json.load(infile)
            if tasks:
                print("This if your task(s) :")
                for elem in tasks:
                    print("ID :", elem["id"], "/ task :", elem["task"])
            else:
                print("No tasks created yet.")
    except FileNotFoundError:
        print("No tasks created yet.")
```

### Fifth step

Add a function for deleting a task.

```
def deleteTask(idTask):
    try:
        idTask = int(idTask)
        with open("tasks.json", "r") as infile:
            tasks = json.load(infile)
            if tasks:
                found = False
                for elem in tasks:
                    if elem["id"] == idTask:
                        found = True
                        tasks = [task for task in tasks if task["id"] != idTask]
                        with open("tasks.json", "w") as outfile:
                            json.dump(tasks, outfile, indent=4)
                        print(f"Task with ID {idTask} deleted successfully.")
                        break
                if not found:
                    print("This ID does not exist.")
            else:
                print("Nothing to delete, there are no tasks yet.")
    except FileNotFoundError:
        print("Nothing to delete, there are no tasks yet.")
    except ValueError:
        print("Invalid ID. Please enter a valid number.")
```

### Sixth step

Adding an update task function.

```
def updateTask(idTask, updatedTask):
    idTask = int(idTask)
    newTask = updatedTask

    try:
        idTask = int(idTask)
        with open("tasks.json", "r") as infile:
            tasks = json.load(infile)
            if tasks:
                found = False
                for elem in tasks:
                    if elem["id"] == idTask:
                        found = True
                        elem["task"] = newTask
                        tasks = [task for task in tasks]
                        with open("tasks.json", "w") as outfile:
                            json.dump(tasks, outfile, indent=4)
                        print(f"Task with ID {idTask} updated successfully.")
                        break
                if not found:
                    print("This ID does not exist.")
            else:
                print("Nothing to update, there are no tasks yet.")
    except FileNotFoundError:
        print("Nothing to update, there are no tasks yet.")
    except ValueError:
        print("Invalid ID. Please enter a valid number.")
```