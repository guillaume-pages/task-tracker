import json

# print("# Adding a new task please")

# task = input()

# dictionary = {
#     "task": task
# }

# json_object = json.dumps(dictionary, indent=4)

# with open("task.json", "w") as outfile:
#     outfile.write(json_object)

def addTask(task):
    print(task)



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