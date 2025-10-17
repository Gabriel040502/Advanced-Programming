task = []
i = 1
while i < 2:
    addtask = input("Enter a name for a your task")
    createdate = input("Enter the creation date of the task")
    duedate = input("Enter the due date of the task")
    task.append(addtask)
    task.append(createdate)
    task.append(duedate)
    print(task)

    print("Press 1 to change the name of your task")
    print("Press 2 to change the creation date of the task")
    print("Press 3 to change the due date of the task")

    choice = input("Enter a number")

    if choice == "1":
        newtask = input("Enter what you would like to change the task to")
        task[0] = (newtask)
        print(task)
    elif choice == "2":
        newcreation = input("Enter what you would like to change the creation date to")
        task[1] = (newcreation)
        print(task)
    elif choice == "3":
        newdue = input("Enter what you would like to change the due date to")
        task[2] = (newdue)
        print(task)
    else:
        print("mission failed")

    