import time
# ----------- Note: ------------
# IV stands for Input Validation

studentData = [ # (5-8) Default student data
    ["john", 1, 70], ["sam", 2, 66], ["elise", 1, 36], ["zoe", 1, 84],
    ["Max", 2, 36],  ["name2", 3, 36], ["name", 2, 86], ["Greg", 3, 96]
]

PRINT_STATEMENTS = [ # (10-16) Print statement dictionary
    "Please enter a number greater than 0",
    "Please enter a number from the list",
    "Sorry that item does not exist",
    "Please enter a NCEA level between 1 and 3",
    "remain in program (enter no to return menu)"
]


def start(): # Menu Function
    print("--------------")
    print("NCEA INTERFACE")
    print("--------------")
    print()
    print("Menu:")
    print("[1] - Total NCEA Summary")
    print("[2] - NCEA Pass Summary")
    print("[3] - Add Credits to Student Data")
    print("[4] - Add New Student")
    print("[5] - Remove Student")
    print("[6] - End Program")
    while True: # (31-35) Asks the user which function they would like to go to
        try:
            menuAnswer = int(input(
                "Enter the number of the menu item you would like to go to: "
                ))
            break
        except ValueError: # IV for preventing alphabetical characters being entered
            print("Please enter an integer between 1 and 7")
    if menuAnswer == 1:
        print("Total NCEA Summary selected")
        totalSummary()
    elif menuAnswer == 2:
        print("NCEA Pass Summary selected")
        passSummary()
    elif menuAnswer == 3:
        print("Add Credit to Student Data selected")
        addCredits()
    elif menuAnswer == 4:
        print("Add New Student selected")
        addStudent()
    elif menuAnswer == 5:
        print("Remove Student selected")
        removeStudents()
    elif menuAnswer == 6:
        print("End Program selected")
        endProgram()
    else:
        print('\033c')  # (58-59) Clears everything outputted above it
        print('\x1bc')
        print("Enter an integer between 1 and 6") 
        start() # Restarts the program


def totalSummary():
    menuString = "create a total summary"
    menuReturnQuery(menuString)
    for i in range(len(studentData)): # (67-68) Prints out all students data
        print("• ", studentData[i][0], ", NCEA Level", studentData[i][1], ",", studentData[i][2], "Credits")
    while True:
        time.sleep(5) # Sleeps the program so the user can process data
        menuString = PRINT_STATEMENTS[4]
        menuReturnQuery(menuString)


def passSummary():
    menuString = "create a pass summary"
    menuReturnQuery(menuString)
    levelOneList = []
    levelTwoList = []
    levelThreeList = []
    for i in range(len(studentData)): # (81-87) Seperates student data into NCEA level lists
        if studentData[i][1] == 1:
            levelOneList.append(studentData[i])
        elif studentData[i][1] == 2:
            levelTwoList.append(studentData[i])
        elif studentData[i][1] == 3:
            levelThreeList.append(studentData[i])
        for i in range(len(levelOneList)): # (88-96) Removes student who have less credits than required
            if levelOneList[i][2] < 80:
                levelOneList.pop(i)
        for i in range(len(levelTwoList)):
            if levelTwoList[i][2] < 60:
                levelTwoList.pop(i)
        for i in range(len(levelThreeList)):
            if levelThreeList[i][2] < 60:
                levelThreeList.pop(i)
    for i in range(len(levelOneList)): # (97-111) Formats and prints the students that have passed each NCEA level
        name = (str(levelOneList[i][0]))
        credits = (int(levelOneList[i][2]))
        level = (int(levelOneList[i][1]))
        print(name, "will pass level", level, "with", credits, "credits")
    for i in range(len(levelTwoList)):
        name = (str(levelTwoList[i][0]))
        credits = (int(levelTwoList[i][2]))
        level = (int(levelTwoList[i][1]))
        print(name, "will pass level", level, "with", credits, "credits")
    for i in range(len(levelThreeList)):
        name = (str(levelThreeList[i][0]))
        credits = (int(levelThreeList[i][2]))
        level = (int(levelThreeList[i][1]))
        print(name, "will pass level", level, "with", credits, "credits")
    menuString = PRINT_STATEMENTS[4]
    menuReturnQuery(menuString) # Return to menu function


def addCredits():
    menuString = "add credits to a students NCEA data"
    menuReturnQuery(menuString)
    num = 1
    for i in studentData: # (120-122) Prints a list of students
        print(num, i[0])
        num += 1
    while True: # (123-139) Asks the user which student they would like to add credits to, includes alphabetical character IV and list range IV
        studentDataItem = 0
        validPrint = 0
        while True:
            if studentDataItem <= 0 or studentDataItem > len(studentData):
                if validPrint == 1:
                    print(PRINT_STATEMENTS[1])
                while True:
                    try:
                        studentDataItem = int(input("Enter the number of the student you want to add credits to: "))
                        break
                    except ValueError:
                        print(PRINT_STATEMENTS[1])
                validPrint = 1
            else:
                break
        break
    addCreditNum = 0
    validPrint = 0
    while True: # (123-139) Asks the user how many credits they would like to add, includes alphabetical character IV and interger range IV
        if addCreditNum <= 0:
            if validPrint == 1:
                print(PRINT_STATEMENTS[0])
            while True:
                try:
                    addCreditNum = int(input(
                        "Enter the amount of credits you would like to add: "
                        ))
                    break
                except ValueError:
                    print(PRINT_STATEMENTS[0])
            validPrint = 1
        else:
            break
    studentDataItem = studentDataItem - 1
    studentData[studentDataItem][2] += addCreditNum # Adds new data to the student's data
    print("New Data is: ", studentData[studentDataItem]) # Shows user the new data that has been added
    menuString = PRINT_STATEMENTS[4]
    menuReturnQuery(menuString) # Return to menu function


def addStudent(): # This function is used to prevent the 'menuReturnQuery' function from repeating if the 'addStudentValidation' is repeated
    menuString = "add a new student"
    menuReturnQuery(menuString)
    addStudentValidation()


def addStudentValidation():
    newStudentData = []
    studentLevel = 0
    validPrint = 0
    studentName = input("Enter Students Name: ").lower()
    newStudentData.append(studentName)
    while True:
        if studentLevel <= 0 or studentLevel >= 4:
            if validPrint == 1:
                print("Please enter a NCEA level between 1 and 3")
            while True:
                try:
                    studentLevel = int(input("Enter Students NCEA Level: "))
                    break
                except ValueError:
                    print("Please enter a NCEA level between 1 and 3")
            validPrint = 1
        else:
            break
    newStudentData.append(studentLevel)
    studentCredits = 0
    validPrint = 0
    while True:
        if studentCredits <= 0:
            if validPrint == 1:
                print(PRINT_STATEMENTS[0])
            while True:
                try:
                    studentCredits = int(input(
                        "Enter the amount of credits this student has: "
                        ))
                    break
                except ValueError:
                    print(PRINT_STATEMENTS[0])
            validPrint = 1
        else:
            break
    newStudentData.append(studentCredits)
    print("Data:", newStudentData)
    while True:
        menuValid = input("Is This Data Correct? ").lower()
        if menuValid == "no":
            print("Restarting Add Student Process")
            addStudentValidation()
        elif menuValid == "yes":
            break
        else:
            print("Please enter [yes] or [no]")
    studentData.append(newStudentData)
    print("Student Data has been added")
    menuString = PRINT_STATEMENTS[4]
    menuReturnQuery(menuString)


def removeStudents():
    menuString = "remove a student"
    menuReturnQuery(menuString)
    num = 1
    for i in studentData:
        print(num, i[0])
        num += 1
    while True:
        try:
            studentDataItem = 0
            validPrint = 0
            while True:
                if studentDataItem <= 0:
                    if validPrint == 1:
                        print(PRINT_STATEMENTS[1])
                    while True:
                        try:
                            studentDataItem = int(input(
                                "Enter the number of the student you want to remove: "
                            ))
                            break
                        except ValueError:
                            print(PRINT_STATEMENTS[1])
                    validPrint = 1
                else:
                    break
            studentData.pop(studentDataItem - 1)
            break
        except IndexError:
            print('Sorry that item does not exist')
    print("Student was removed from the list")
    menuString = PRINT_STATEMENTS[4]
    menuReturnQuery(menuString)


def endProgram():
    menuString = "end program"
    menuReturnQuery(menuString)
    print('\033c')  # Clears everything outputted above it
    print('\x1bc')
    print("Ended Program")


def menuReturnQuery(menuString):
    if menuString == "remain in program (enter no to return menu)":
        queryString = "Do"
    else:
        queryString = "Are you sure"
    while True:
        menuValid = input(
            "{} you want to {}: [yes]/[no] ".format(queryString, menuString)
            ).lower()
        if menuValid == "no":
            print('\033c')  # Clears everything outputted above it
            print('\x1bc')
            start()
        elif menuValid == "yes" and menuString != "remain in program (enter no to return menu)":
            break
        elif menuValid == "yes" and menuString == "remain in program (enter no to return menu)":
            time.sleep(5)
            menuReturnQuery(menuString)
        else:
            print("Please enter [yes] or [no]")
    return

start()
