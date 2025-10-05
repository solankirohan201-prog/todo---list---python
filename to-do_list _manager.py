tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append({'task': task, 'done': False})
        print("Task added.")
    elif choice == '2':
        for i, t in enumerate(tasks):
            status = "✔" if t['done'] else "✘"
            print(f"{i+1}. {t['task']} [{status}]")
    elif choice == '3':
        num = int(input("Enter task number to mark done: "))
        if 0 < num <= len(tasks):
            tasks[num-1]['done'] = True
            print("Task marked as completed.")
    elif choice == '4':
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted.")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
