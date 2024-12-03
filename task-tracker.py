import json

###########################
# Function for add a task #
###########################
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

###############################
# Function for list the tasks #
###############################
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

##############################
# Function for delete a task #
##############################
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

##########################
# Function update a task #
##########################
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

#################
# Function main #
#################
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