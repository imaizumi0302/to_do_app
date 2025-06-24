features_list = ["1.-Add Task", "2.-Remove Task", "3.-View Task", "4.-Exit"]
print("To-Do list App")
while True:
    for feature in features_list:
        print(feature)
    choice = input("What would you like to do?: ")
    to_do_list=[]
    if choice == "1":
        new_task = input("Add a new task:")
        to_do_list.append(new_task)
    else:
        break
