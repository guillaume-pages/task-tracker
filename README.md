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

# My solution

## How to use

Make sur you have python install on your machine.

Download the code and run this command :

```
python3 task-tracker.py
```

The outpout will be :

```
Welcome to Task Tracker CLI !

For beggining write the command add follow 
by your task to add a new task it into our tool.

Use the command "help" for the list of available commands.

=>
```

## First step

Try to write on the terminal and read a value write by a user.

<details>
    <summary>Code</summary>


```python
print("Hello user, what is your name ?")

name = input()
print("Greetings", name, "!")
```
</details>

<details>
    <summary>Outpout</summary>

```
python3 task-tracker.py
Hello user, what is your name ?
Guillaume
Greatings Guillaume !
```

</details>

## Second step 

Take the user entry and put the value into a json file.

<details>
    <summary>Code</summary>

```python
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
</details>

<details>
    <summary>Outpout</summary>

```json
{
    "task": "First task"
}
```
</details>

## Third step

Create a command line application that will wait for instructions.

<details>
    <summary>Code</summary>

```python
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
</details>

<details>
    <summary>Outpout</summary>

```
python3 task-tracker.py
Welcome to Task Tracker CLI !

For beggining write the command add follow 
by your task to add a new task it into our tool.

Use the command "help" for the list of available commands.

=> 
```
</details>

## Fourth step

Add a function for write multiple task and a command for listing all the tasks.

<details>
    <summary>Code</summary>

```python
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
</details>

## Fifth step

Add a function for deleting a task.

<details>
    <summary>Code</summary>

```python
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
</details>

<details>
    <summary>Outpout</summary>

```
python3 task-tracker.py
Welcome to Task Tracker CLI !

For beggining write the command add follow 
by your task to add a new task it into our tool.

Use the command "help" for the list of available commands.

=> delete 4
Task with ID 4 deleted successfully.
=> 
```
</details>

## Sixth step

Adding an update task function.

<details>
    <summary>Code</summary>

```python
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
</details>

<details>
    <summary>Outpout</summary>

```
=> list
This if your task(s) :
ID : 1 / task : example task / status : done
=> update 1 Task updated
Task with ID 1 updated successfully.
=> list
This if your task(s) :
ID : 1 / task : Task updated / status : done
=>
```
</details>

## Seventh step

Add the option for the command list, the options are todo, in-progress and done.

<details>
    <summary>Code</summary>

```python
def taskListWithOption(*arg):
    status = arg[0]

    try:
        if status == "todo":
            with open("tasks.json", "r") as infile:
                tasks = json.load(infile)
                if tasks:
                    print("This are the task with a todo status :")
                    for task in tasks:
                        if task["status"] == "todo":
                            print("ID :", task["id"], "/ task :", task["task"], "/ status :", task["status"])
        elif status == "done":
            with open("tasks.json", "r") as infile:
                tasks = json.load(infile)
                if tasks:
                    print("This are the task with a done status :")
                    for task in tasks:
                        if task["status"] == "done":
                            print("ID :", task["id"], "/ task :", task["task"], "/ status :", task["status"])
        elif status == "in-progress":
            with open("tasks.json", "r") as infile:
                tasks = json.load(infile)
                if tasks:
                    print("This are the task with a in-progress status :")
                    for task in tasks:
                        if task["status"] == "in-progress":
                            print("ID :", task["id"], "/ task :", task["task"], "/ status :", task["status"])
        else:
            print("This command option is not available")
    except FileNotFoundError:
        print("No tasks created yet")
```
</details>

## Eighth step

Add a function for update the status of a specific task

<details>
    <summary>Code</summary>

```python
def updateTaskStatus(status, idTask):
    if not isinstance(idTask, int):
        print("Error: you must enter a valid number for the ID task.")
        return

    try:
        with open("tasks.json", "r") as infile:
            tasks = json.load(infile)
    except FileNotFoundError:
        print("Nothing to update, there are no tasks yet.")
        return

    task_found = False
    for task in tasks:
        if task["id"] == idTask:
            task["status"] = status
            task_found = True
            break

    if not task_found:
        print(f"Error: Task with ID {idTask} not found.")
        return

    with open("tasks.json", "w") as outfile:
        json.dump(tasks, outfile, indent=4)

    print(f"Task with ID {idTask} updated successfully to status '{status}'.")
```
</details>