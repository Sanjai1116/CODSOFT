# To-Do List Application

todo_list = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added!")
    
    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i in range(len(todo_list)):
                print(f"{i+1}. {todo_list[i]}")
    
    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to remove!")
        else:
            print("\nYour Tasks:")
            for i in range(len(todo_list)):
                print(f"{i+1}. {todo_list[i]}")
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number!")
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice, try again!")