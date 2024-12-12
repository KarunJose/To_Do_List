import sys

todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_todo_list():
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task you want to add: ")
    todo_list.append(task)
    print(f"'{task}' has been added to your to-do list.")

def remove_task():
    view_todo_list()
    if todo_list:
        task_number = int(input("Enter the number of the task you want to remove: "))
        if 0 < task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number!")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            view_todo_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the to-do list application. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
