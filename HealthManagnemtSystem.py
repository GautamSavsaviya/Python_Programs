# function for get current date and time
def getdate():
    import datetime
    return datetime.datetime.now()


# function for log diet into file
def logdiet(name, time, food):
    with open(name + "Diet.txt", "a") as f:
        f.write("[" + str(time) + "]\t" + food + '\n')
    message = "Your data is loged successfully... ! "
    return message


# function for log exersice into file
def logexersice(name, time, exersice):
    with open(name + "Exersice.txt", "a") as f:
        f.write("[" + str(time) + "]\t" + exersice + '\n')
    message = "Your data is loged successfully... ! "
    return message


# function for retrieve diet data
def retievediet(name):
    try:
        with open(name + "Diet.txt", "r") as f:
            content = f.read()
    except Exception as e:
        # noinspection PyTypeChecker
        content = "Error: " + str(e)
    return content


# function for retrieve diet data
def retieveexersice(name):
    try:
        with open(name + "Exersice.txt") as f:
            content = f.read()
    except Exception as e:
        content = "Error: " + str(e)
    return content


while True:
    print("Enter your client name: ", end="")
    name = input()
    print("Enter a number '1' for log data or '2' for retrieve data: ", end="")
    choice = int(input())
    if choice == 1:
        print("Enter 'd' for log diet or 'e' for log exersice: ", end="")
        item = input()
        if item == "d":
            print("Enter your diet name: ", end="")
            food = input()
            time = getdate()
            message = logdiet(name, time, food)
            print(message)
        elif item == "e":
            exersice = input("Enter exersice name: ")
            time = getdate()
            message = logexersice(name, time, exersice)
            print(message)
    elif choice == 2:
        print("Enter 'd' for log diet or 'e' for log exersice: ", end="")
        item = input()
        if item == "d":
            content = retievediet(name)
            print(content)
        elif item == "e":
            content = retieveexersice(name)
            print(content)
    else:
        print("You enter Wrong choice, please reenter your choice")

    print("For exit, Press '0' otherwise press '1'")
    close = int(input())
    if close == 0:
        exit()
