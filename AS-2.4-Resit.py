import time

studentData = [
    ["name", 1, 36], ["name", 2, 36], ["name", 1, 36], ["name", 2, 36], ["name", 2, 36], ["name", 3, 36], ["name", 2, 36], ["name", 3, 36]
]

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
    menuReturnQuery(menuString)
    for i in range(len(studentData)):
        print("• ", studentData[i][0], ", NCEA Level", studentData[i][1], ",", studentData[i][2], "Credits")
    time.sleep(5)
    menuString = "remain in program"
    menuReturnQuery(menuString)
    

def passSummary():
    menuString = "create a pass summary"
    menuReturnQuery(menuString)
    levelOneList = []
    levelTwoList = []
    levelThreeList = []
    for i in range(len(studentData)):
        if studentData[i][1] == 1:
            levelOneList.append(studentData[i])
            print(levelOneList)
        elif studentData[i][1] == 2:
            levelTwoList.append(studentData[i])
            print(levelTwoList)
        elif studentData[i][1] == 3:
            levelThreeList.append(studentData[i])
            print(levelThreeList)
        print(levelOneList)
        print(levelTwoList) #Console statement
        print(levelThreeList)
        for i in range(len(levelOneList)):
            if levelOneList[i][2] < 60:
                levelOneList.pop(levelOneList[i]) 
            print(levelOneList)


def yearSummary():
    menuString = "create a NCEA level summary"
    menuReturnQuery(menuString)
    print("yay")

def addCredits():
    menuString = "add credits to student data"
    menuReturnQuery(menuString)
    print("yay")

def addStudent():
    menuString = "add a new student"
    menuReturnQuery(menuString)
    print("yay")

def removeStudents():
    menuString = "remove a student"
    menuReturnQuery(menuString)
    print("yay")

def endProgram():
    menuString = "end program"
    menuReturnQuery(menuString)
    print('\033c')  #Clears everything outputted above it
    print('\x1bc')
    print("Ended Program")

def menuReturnQuery(menuString):
    if menuString == "remain in program":
        queryString = "Do"
    else:
        queryString = "Are you sure"
    while True:
        menuValid = input("{} you want to {}: ".format(queryString, menuString)).lower()
        if menuValid == "no":
            print('\033c')  #Clears everything outputted above it
            print('\x1bc')
            start()
        elif menuValid == "yes":
            break
        else:
            print("Please enter [yes] or [no]")
    return

start()