from datetime import datetime
#task_list = [('buy', 1, '2025-07-01'), ('sell', 2, '2025-06-30'), ('push', 3, '2025-06-29'), ('say', 1, '2025-06-27'), ('ask', 2, '2025-06-26')]
task_list = []

def add_task():
    task_name = input("Add a task: ")
    task_priority = int(input("Enter the priority of the task as a number (1 = High, 2 = Medium, 3 = Low): "))

    # Validate date format
    while True:
        task_due = input("Enter the due date of the task (YYYY-MM-DD): ")
        try:
            datetime.strptime(task_due, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    new_task = (task_name, task_priority, task_due)
    task_list.append(new_task)
    print(f"Your remaining tasks: {task_list}")

def remove_task():
    while True:
        answer = input("Do you want to remove the task?(y/n)")
        if not (answer == "y" or answer == "n"):
            print("You entered wrong answer. You have to enter 'y' or 'n'")
            continue
        if answer == 'y':
            for i,task in enumerate(task_list):
                print(f"{i}. {task}")
            task_number = int(input("type a task number you remove:"))
            if not task_number in range(len(task_list)):
                print("Invalid input")
                continue
            elif task_number in range(len(task_list)):
                removed = task_list.pop(task_number)
                print(f"You removed [{removed}]")
                print(f"your remaining task:{task_list}")
                break
            else: task
        else:
            print("Returning to the menu")
            break


def view_tasks():
    print("Your remaining tasks sorted by priority and due date:")
    task_sorted = sorted(task_list, key=lambda task: (task[1], task[2]))  # sort by priority desc, date asc
    for task in task_sorted:
        print(f"- {task}")


def suggest_task():
    print("Here are suggested tasks you might want to work on:")
    task_sorted = sorted(task_list, key = lambda priority: (priority[1],priority[2]))

    today = datetime.today().date()
    for task in task_sorted:
            deadline = datetime.strptime(task[2],"%Y-%m-%d").date()
            diff = deadline - today
            if diff.days <= 5 or task[1] == 1:
                print(f"- {task}")

features_list = ["1.-Add Task", "2.-Remove Task", "3.-View Task", "4.-Suggested Tasks" , "5.-Exit"]
while True:
    print("To-Do list App")
    for feature in features_list:
        print(feature)
    number = input("Enter your number:")
    if not number in ["1", "2", "3", "4", "5"]:
        print("Invalid input.")
        continue
    else:
        if number == "1":
            add_task()

        elif number == "2":
            remove_task()

        elif number == "3":
            view_tasks()

        elif number == "4":
            suggest_task()

        elif number == "5":
            print("Exiting the application. Good bye!")
            break

