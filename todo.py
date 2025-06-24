task_list = []

def add_task():
    task_name = input("Add a task:")
    task_list.append(task_name)
    print(f"your remaining task:{task_list}")


def remove_task():
    task_name = input("type a task you remove:")
    task_list.remove(task_name)
    print(f"your remaining task:{task_list}")

# def view_tasks():

features_list = ["1.-Add Task", "2.-Remove Task", "3.-View Task", "4.-Exit"]
print("To-Do list App")
while True:
    for feature in features_list:
        print(feature)
    number = input("Enter your number:")
    if not number in ["1","2","3","4"]:
        print("Invalid input.")
        continue
    else:
        if number == "1":
            add_task()

        elif number == "2":
            remove_task()

        elif number == "3":
            view_task()

        elif number == "4":
            print("Exiting the application. Good bye!")
            break