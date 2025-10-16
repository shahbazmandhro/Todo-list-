shahbaz_tasks = []

def shahbaz_view_tasks():
    if not shahbaz_tasks:
        print("\nNo Tasks available:\n")
    else:
        print("\nYour Tasks:")
        for shahbaz_task_no, shahbaz_task in enumerate(shahbaz_tasks, 1):
            print(f"{shahbaz_task_no}. {shahbaz_task}")
        print()

def shahbaz_add_task():
    shahbaz_task = input("Enter new task: ")
    shahbaz_tasks.append(shahbaz_task)
    print("Task added successfully!")

def shahbaz_update_task():
    shahbaz_view_tasks()
    if not shahbaz_tasks:
        return
    try:
        shahbaz_task_no = int(input("Enter task number to update: "))
        if 1 <= shahbaz_task_no <= len(shahbaz_tasks):
            shahbaz_new_task = input("Enter updated task: ")
            shahbaz_tasks[shahbaz_task_no - 1] = shahbaz_new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def shahbaz_delete_task():
    shahbaz_view_tasks()
    if not shahbaz_tasks:
        return
    try:
        shahbaz_task_no = int(input("Enter task number to delete: "))
        if 1 <= shahbaz_task_no <= len(shahbaz_tasks):
            shahbaz_removed = shahbaz_tasks.pop(shahbaz_task_no - 1)
            print(f"Task '{shahbaz_removed}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def shahbaz_main():
    while True:
        print("\nTodo List (Shahbaz)")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        shahbaz_choice = input("Enter your choice: ")

        if shahbaz_choice == "1":
            shahbaz_view_tasks()
        elif shahbaz_choice == "2":
            shahbaz_add_task()
        elif shahbaz_choice == "3":
            shahbaz_update_task()
        elif shahbaz_choice == "4":
            shahbaz_delete_task()
        elif shahbaz_choice == "5":
            print("Goodbye Shahbaz!")
            break
        else:
            print("Invalid choice. Please try again.")

shahbaz_main()