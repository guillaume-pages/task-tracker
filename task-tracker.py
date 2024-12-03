import json

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
            task = input()
            addTask(task)
        elif command == "list":
            tasksList()
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