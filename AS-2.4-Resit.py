
def start():
    print("--------------")
    print("NCEA INTERFACE")
    print("--------------")
    print()
    print("Menu:")
    print("[1] - Total NCEA Summary")
    print("[2] - NCEA Pass Summary")
    print("[3] - NCEA Level Summary")
    print("[4] - Add Credits to Student Data")
    print("[5] - Add New Student")
    print("[6] - Remove Student")
    print("[7] - End Program")
    while True:
        try:
            menuanswer = int(input("Enter the number of the menu item you would like to go to: "))
            break
        except ValueError:
            print("Please enter an integer between 1 and 7")
    if menuanswer == 1:
        print("Total NCEA Summary selected")
        totalSummary()
    elif menuanswer == 2:
        print("NCEA Pass Summary selected")
        passSummary()
    elif menuanswer == 3:
        print("NCEA Level Summary selected")
        yearSummary()
    elif menuanswer == 4:
        print("Add Credit to Student Data selected")
        addCredits()
    elif menuanswer == 5:
        print("Add New Student selected")
        addStudent()
    elif menuanswer == 6:
        print("Remove Student selected")
        removeStudents()
    elif menuanswer == 7:
        print("End Program selected")
        endProgram()
    else:
        print("Enter an integer between 1 and 7")
        print('\033c')  #Clears everything outputted above it
        print('\x1bc')
        start()

def totalSummary():
    menuString = "create a total summary"
    print("Total Summary")
    print()
    menuValidation(menuString)
    print("yay")

def passSummary():
    menuString = "create a pass summary"
    print("NCEA Pass Summary")
    print()
    menuValidation(menuString)
    print("yay")

def yearSummary():
    menuString = "create a NCEA level summary"
    print("NCEA Level Summary")
    print()
    menuValidation(menuString)
    print("yay")

def addCredits():
    menuString = "add cridts to student data"
    print("Add Credits to Student Data")
    print()
    menuValidation(menuString)
    print("yay")

def addStudent():
    menuString = "add a new student"
    print("Add New Student")
    print()
    menuValidation(menuString)
    print("yay")

def removeStudents():
    menuString = "remove a student"
    print("Remove Student")
    print()
    menuValidation(menuString)
    print("yay")

def endProgram():
    menuString = "end program"
    menuValidation(menuString)
    print("yay")

def menuValidation(menuString):
    while True:
        menuValid = input("Are you sure you want to {}: ".format(menuString)).lower()
        if menuValid == "no":
            start()
        elif menuValid == "yes":
            break
        else:
            print("Please enter [yes] or [no]")
    return

start()