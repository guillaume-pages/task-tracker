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

    tasks.append({"id": id, "task": task, "status": "todo"})

    with open("tasks.json", "w") as outfile:
        json.dump(tasks, outfile, indent=4)

    print("Task added successfully (ID:", id,")")

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
                    print("ID :", elem["id"], "/ task :", elem["task"], "/ status :", elem["status"])
            else:
                print("No tasks created yet.")
    except FileNotFoundError:
        print("No tasks created yet.")

##############################################
# Function for list the tasks with an option #
##############################################
def taskListWithOption(*arg):
    status = arg[0]

    try:
        if status == "todo":
            with open("tasks.json", "r") as infile:
                tasks = json.load(infile)
                if tasks:
                    tasks_to_print = [task for task in tasks if task["status"] == "todo"]
                    print("Task(s) with a status todo :\n")
                    for task in tasks_to_print:
                        print("- ID :", task["id"], "/ task :", task["task"], "/ status :", task["status"])
        elif status == "in-progress":
            with open("tasks.json", "r") as infile:
                tasks = json.load(infile)
                if tasks:
                    tasks_to_print = [task for task in tasks if task["status"] == "in-progress"]
                    print("Task(s) with a status in-progress :\n")
                    for task in tasks_to_print:
                        print("- ID :", task["id"], "/ task :", task["task"], "/ status :", task["status"])
        elif status == "done":
            with open("tasks.json", "r") as infile:
                tasks = json.load(infile)
                if tasks:
                    tasks_to_print = [task for task in tasks if task["status"] == "done"]
                    print("Task(s) with a status done :\n")
                    for task in tasks_to_print:
                        print("- ID :", task["id"], "/ task :", task["task"], "/ status :", task["status"])
        else:
            print("This command option is not available")
    except FileNotFoundError:
        print("No tasks created yet")

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

#################################
# Function update a status task #
#################################
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
                        idTask = command[7:].strip()
                        deleteTask(idTask)
                    else:
                        print("You have no task yet, they are nothing to delete")
            except FileNotFoundError:
                print("You have no task yet, they are nothing to delete")
        elif command == "list":
            tasksList()
        elif command.startswith("list "):
            status = command[5:].strip()
            if " " in status:
                print("You must enter only one option after the command list.")
            elif len(status) > 1:
                taskListWithOption(status)
            else:
                tasksList()
        elif command.startswith("update "):
            parts = command[7:].split(" ", 1)
            if len(parts) < 2:
                print("Error : Command invalid. Expected : update [ID] [new task]")
            else:
                idTask = parts[0].strip()
                updatedTask = parts[1].strip()
                updateTask(idTask, updatedTask)
        elif command.startswith("mark "):
            parts = command[5:].split(" ")
            if len(parts) < 2:
                print("Error: Command invalid. Expected: mark [option] [ID]")
            else:
                option_candidate = parts[0].strip()
                id_candidate = parts[1].strip()
                valid_statuses = {"done", "in-progress"}
                if option_candidate not in valid_statuses:
                    try:
                        int(option_candidate)
                        print("Error: Command invalid. Did you mean: mark [option] [ID]?")
                    except ValueError:
                        print(f"Error: '{option_candidate}' is not a valid status. Allowed values are: done and in-progress.")
                else:
                    try:
                        idTask = int(id_candidate)
                        updateTaskStatus(option_candidate, idTask)
                    except ValueError:
                        print(f"Error: '{id_candidate}' is not a valid task ID (number).")
        elif command == "help":
            print("""
This are the command availables :
    - add : add your task in our system
    - delete [ID] : delete a task by enter is ID
    - exit : terminate the application
    - list [option] : list all your tasks, this are the option available :
        - todo : list all the tasks with a status todo
        - done : list all the tasks with a status done
        - in-progress : list all the tasks with a status in-progress
    - mark [option] [ID] : update the status of a specific task
        - in-progress
        - done
    - update [ID] [task] : update a task by enter is ID and your new sentence
""")
        else:
            print("Command not found. Use help for a list of command availables.")

if __name__ == "__main__":
    main()