import time

studentData = [
    ["john", 1, 70], ["sam", 2, 66], ["elise", 1, 36], ["zoe", 1, 84], ["Max", 2, 36], ["name2", 3, 36], ["name", 2, 86], ["Greg", 3, 96]
]

def start():
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
        print("Add Credit to Student Data selected")
        addCredits()
    elif menuanswer == 4:
        print("Add New Student selected")
        addStudent()
    elif menuanswer == 5:
        print("Remove Student selected")
        removeStudents()
    elif menuanswer == 6:
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
    while True:
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
            if levelOneList[i][2] < 80:
                levelOneList.pop(i) 
        for i in range(len(levelTwoList)):
            if levelTwoList[i][2] < 60:
                levelTwoList.pop(i) 
        for i in range(len(levelThreeList)):
            if levelThreeList[i][2] < 60:
                levelThreeList.pop(i) 
    passList = []
    for i in range(len(levelOneList)):
        name = (str(levelOneList[i][0]))
        credits = (int(levelOneList[i][2]))
        level = (int(levelOneList[i][1]))
        print(name, "will pass level",level , "with", credits, "credits")
    for i in range(len(levelTwoList)):
        name = (str(levelTwoList[i][0]))
        credits = (int(levelTwoList[i][2]))
        level = (int(levelTwoList[i][1]))
        print(name, "will pass level",level , "with", credits, "credits")
    for i in range(len(levelThreeList)):
        name = (str(levelThreeList[i][0]))
        credits = (int(levelThreeList[i][2]))
        level = (int(levelThreeList[i][1]))
        print(name, "will pass level",level , "with", credits, "credits")
    menuString = "remain in program"
    menuReturnQuery(menuString)

def addCredits():
    menuString = "add credits to student data"
    menuReturnQuery(menuString)
    for i in range(len(studentData)):
        name = (str(studentData[i][0]))
        print(i + 1, name)
    findStudent = -1
    validPrint = 0
    while True:
        if findStudent <= 0 or findStudent > len(studentData):
            if validPrint == 1:
                print("Please enter a number from the list")
            while True:
                try:
                    findStudent = int(input("Enter the number of the student:"))
                    break
                except ValueError:
                    print("Please enter a number from the list")
            validPrint = 1
        else:
            break
    addCreditsData = studentData[findStudent - 1]
    name = (str(addCreditsData[0]))
    credits = (int(addCreditsData[2]))
    print(addCreditsData)


    
"""
while True:
        if credits -  <= 0 or :
            if validPrint == 1:
                print("Please enter a number from the list")
            while True:
                try:
                    findStudent = int(input("Enter the number of the student:"))
                    break
                except ValueError:
                    print("Please enter a number from the list")
            validPrint = 1
        else:
            break
"""
    

     


            




def addStudent():
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
                print("Please enter an amount greater than 0")
            while True:
                try:
                    studentCredits = int(input("Enter the amount of credits this student has: "))
                    break
                except ValueError:
                    print("Please enter an integer")
            validPrint = 1
        else:
            break
    newStudentData.append(studentCredits)
    print("Data:",newStudentData)
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
    menuString = "remain in program"
    menuReturnQuery(menuString)

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
        elif menuValid == "yes" and menuString != "remain in program":
            break
        elif menuValid == "yes" and menuString == "remain in program":
            time.sleep(5)
            menuReturnQuery(menuString)
        else:
            print("Please enter [yes] or [no]")
    return


start()