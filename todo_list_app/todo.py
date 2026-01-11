import os
import datetime as dt

file = "texts.txt"

print("="*30 + "\nWelcome to your Task Manager\n" + "="*30)

while True:
    print("\n\t1. Add new task.")
    print("\t2. View all tasks.")
    print("\t3. Delete a task.")
    print("\t4. Exit.")

    choice = input("\nChoose a option(1-4): ").strip()

    if choice == '1':
        while True:
            task = input("Enter a task: ").strip()

            if not task:
                print("Error: You cannot save an empty task")
            else:
                timestamp = dt.datetime.now().strftime("%d-%b-%Y %I:%M %p")
                with open(file, 'a') as f:
                    f.write(f"{task} | Added on: {timestamp}\n")
                    print(f"\n--> Task saved to {file}")
                
                exit_task = input("\nDo you want to add another task? (y/n): ").strip().lower()
                if exit_task != 'y':
                    break
    
    elif choice == '2':
        tasks = []
        try:
            with open(file, 'r') as f:
                tasks = f.readlines()

            if not tasks:
                print("\n--> Your list is empty!")
            else:
                print("\n---- Your Saved Task ----")
                for count, line in enumerate(tasks, start=1):
                    print(f"{count}. {line.strip()}")
                
                total_tasks = len(tasks)
                print(f"\nTotal tasks: {total_tasks}")

        except FileNotFoundError:
            print("\n--> No file exists! Add a new task first.")

    elif choice == '3':
        try:
            with open(file, 'r') as f:
                tasks = f.readlines()

            if not tasks:
                print("\n--> Nothing to delete! List is empty.")
            else:
                print("\n---- Select Task to Delete ----")
                for count, line in enumerate(tasks, start=1):
                    print(f"{count}. {line.strip()}")

                choice_del = input("\nEnter task number to delete (or 'c' to cancel): ").strip()

                if choice_del.lower() == 'c':
                    continue
                
                idx = int(choice_del) - 1

                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    total_tasks = len(tasks)

                    with open(file, 'w') as f:
                        f.writelines(tasks)
                    print(f"--> Deleted: {removed.strip().split('|')[0]}")
                    print(f"Remaining tasks: {total_tasks}")
                
                else:
                    print("Invalid task number!")
        
        except FileNotFoundError:
            print("--> No file exists yet.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '4':
        confirm_exit = input("\nAre you sure you want to exit? (y/n): ").strip().lower()
        if confirm_exit == 'y':
            print("Cleaning up... GoodBye!!")
            break
        else:
            print("Return to Main Menu...")

    else:
        print("Invalid Choice. Please Choose 1, 2, 3 or 4.")