import os

file = "texts.txt"

print("="*30 + "\nWelcome to your Task Manager\n" + "="*30)

while True:
    print("\n\t1. Add new task.")
    print("\t2. View all tasks.")
    print("\t3. Exit.")

    choice = input("Choose a option(1-3): ").strip()

    if choice == '1':
        task = input("Enter a task: ").strip()

        if task == '':
            print("Error: You cannot save an empty list")
        else:
            f = open(file, 'a')
            f.write(task + '\n')
            f.close()
            print(f"Task saved to {file}")
    
    elif choice == '2':
        print("\n---- Your Saved Task ----")

        if os.path.exists(file):
            f = open(file, 'r')
            tasks = f.readlines()
            f.close()

            if len(tasks) == 0:
                print("Your list is empty!")
            else:
                count = 1
                for line in tasks:
                    print(f"{count}. {line.strip()}")
                    count += 1
        else:
            print("No file exists! Add a new task.")

    elif choice == '3':
        print("Cleaning up... GoodBye!!")
        break

    else:
        print("Invalid Choice. Please Choose 1, 2, or 3.")