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
    print("Welcome to Task Tracker CLI !")
    print("""For beggining write the commande add follow 
by your task to add a new task it into our tool.
""")

    while True:
        command = input("=> ")

        if command == "exit":
            print("See you soon !")
            break
        elif command == "add":
            print("add a new task below :")
        elif command == "help":
            print("""
This are the command availables :
    - add [your task] : add your task in our system
    - exit : terminate the application
""")
        else:
            print("Command not found. Use help for a list of command availables.")

if __name__ == "__main__":
    main()
```