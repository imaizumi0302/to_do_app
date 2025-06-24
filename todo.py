task_list = []


def add_task():
    task_name = input("Add a task:")
    task_list.append(task_name)
    print(f"your remaining task:{task_list}")


def remove_task():
    while True:
        for i, task in enumerate(task_list):
            print(f"{i}, {task}")
        task_number = int(input("Enter the task to remove:"))

        removed = task_list.pop(task_number)
        print(f"You removed {removed}")
        print(f"your remaining task:{task_list}")


def view_tasks():
    print("Your remaining task:")
    for task in task_list:
        print(f"- {task}")


features_list = ["1.-Add Task", "2.-Remove Task", "3.-View Task", "4.-Exit"]
while True:
    print("To-Do list App")
    for feature in features_list:
        print(feature)
    number = input("Enter your number:")
    if not number in ["1", "2", "3", "4"]:
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
            print("Exiting the application. Good bye!")
