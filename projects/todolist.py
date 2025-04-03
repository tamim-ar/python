tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def remove_task(index):
    if 0 <= index < len(tasks):
        print(f"Removed: {tasks.pop(index)}")
    else:
        print("Invalid index!")

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

while True:
    print("\n1. Add Task\n2. Remove Task\n3. Show Tasks\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
        index = int(input("Enter task number to remove: ")) - 1
        remove_task(index)
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
