import shelve

# EXAMPLE ASSIGNMENT
# assignmentsDict = {
#     'AIST 2120-Project 2': {'name':'Project 2', 'course':'AIST 2120', 'due':'12/4/2020', 'status':'active', 'time':'N/A'}
# }


# USED TO FILTER THE DICTIONARY WHEN VIEWING ACTIVE ASSIGNMENTS
def sortFunction(value):
    name = value['name']
    course = value['course']
    status = value['status']
    date = value['due']
    parts = date.split('/')
    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])
    return (status, year, month, day, course, name)

# USED TO FILTER WHEN VIEWING ALL ASSIGNMENTS
def sortReport(value):
    name = value['name']
    course = value['course']
    date = value['due']
    time = value['time']
    parts = date.split('/')
    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])
    return (time, year, month, day, course, name)

# MENU DESIGN
def menu():
    print("_"*47)
    print(f"|{'PLANNER':^45}|")
    print("-" * 47)
    print('| 1) View Active Assigments')
    print('| 2) View Report (Completed Assignment History)')
    print('| 3) Add an Assignment')
    print('| 4) Edit an Assigment')
    print('| 5) Mark Asignment Completed')
    print('| X) Exit')

    print("-" * 47)

# ADD AN ASSIGNMENT
def addAssignment():
    global assignmentsDict

    print('_' * 47)
    print(f"|{'New Assignment Info':^45}|")
    print('-'*47)
    course = input('| Course Name: ').strip()
    name = input('| Assignment Name: ').strip()
    date = input('| Due Date (i.e. 12/04/2020): ').strip()
    status = 'active'
    time = 'N/A'

    combinedName = f"{course}-{name}"

    newAssignment = {}
    newAssignment['course'] = course
    newAssignment['name'] = name
    newAssignment['due'] = date
    newAssignment['status'] = status
    newAssignment['time'] = time
    
    if combinedName in assignmentsDict.keys():
        print(f'| {name} could not be added\n| Must enter a different assignment name')
        print('-'*47)
    else:
        assignmentsDict[combinedName] = newAssignment
        print(f"| {name} was added.")
        print('-'*47)

# VIEW ACTIVE ASSIGNMENTS
def viewAssignments():
    global assignmentsDict
    
    print("_"*67)
    print(f"|{'ASSIGNMENTS':^65}|")
    print("-" * 67)
    print(f"|{'Course':<15}{'Assignment Name':<25}{'Due Date':15}{'Status':>10}|")
    print("-"*67)

    sorted_assignments = sorted(assignmentsDict.values(), key=sortFunction)
    for assignment in sorted_assignments:
        if assignment['status'] == 'complete':
            continue
        else:
            print(f"|{assignment['course']:<15}{assignment['name']:<25}{assignment['due']:15}{assignment['status']:>10}|")
    print('-'*67)

# EDIT AN ASSIGNMENT
def editAssignment():
    global assignmentsDict
    
    print("_"*82)
    print(f"|{'ASSIGNMENTS':^80}|")
    print("-" * 82)
    print(f"|{'Course':<15}{'Assignment Name':<25}{'Due Date':15}{'Status':<10}{'Time Spent':>15}|")
    print("-"*82)

    sorted_report_assignments = sorted(assignmentsDict.values(), key=sortReport)
    for assignment in sorted_report_assignments:
        print(f"|{assignment['course']:<15}{assignment['name']:<25}{assignment['due']:15}{assignment['status']:<10}{assignment['time']:>15}|")
    print('='*82)
    
    
    toEdit = input('|Which assignment would you like to edit? ').strip()

    editAssignment = assignmentsDict[toEdit]
    currentCourse = editAssignment['course']
    currentName = editAssignment['name']
    currentDate = editAssignment['due']
    currentStatus = editAssignment['status']
    currentTime = editAssignment['time']

    updatedCourse = input('|Course Name: ').strip()
    updatedName = input('|Assignment Name: ').strip()
    updatedDate = input('|Due Date (i.e. month, day, year): ').strip()
    updatedStatus = input('|Status: ').strip()
    updatedTime = input('|Time spent: ').strip()

    if len(updatedCourse) == 0:
        updatedCourse = currentCourse
    if len(updatedName) == 0:
        updatedName = currentName
    if len(updatedStatus) == 0:
        updatedStatus = currentStatus
    if len(updatedTime) == 0:
        updatedTime = currentTime
    if updatedDate == '':
        newDate = currentDate
    else:
        newDate = updatedDate

    updatedAssignment = {}
    updatedAssignment['course'] = updatedCourse
    updatedAssignment['name'] = updatedName
    updatedAssignment['due'] = newDate
    updatedAssignment['status'] = updatedStatus
    updatedAssignment['time'] = updatedTime

    assignmentsDict[toEdit] = updatedAssignment
    print(f"|{toEdit} has successfully been edited.")
    print("-" * 67)

# MARK AN ASIGNMENT COMPLETED
def markComplete():
    global assignmentsDict
    viewAssignments()
    markDone = input('|Which assignment would you like to mark complete? ').strip()
    timeSpent = input(f"|Time spent completing {markDone} [OPTIONAL]: ").strip()

    markComplete = assignmentsDict[markDone]
    currentCourse = markComplete['course']
    currentName = markComplete['name']
    currentDate = markComplete['due']

    completedAssignment = {}
    completedAssignment['course'] = currentCourse
    completedAssignment['name'] = currentName
    completedAssignment['due'] = currentDate
    completedAssignment['status'] = 'complete'
    if len(timeSpent) == 0:
        completedAssignment['time'] = 'N/A'
    else:
        completedAssignment['time'] = timeSpent

    assignmentsDict[markDone] = completedAssignment
    print(f"|{markDone} was successfully marked as complete.")
    print("-" * 67)
    
# VIEW PAST/COMPLETED ASIGNMENTS
def viewReport():
    global assignmentsDict
    print("_"*82)
    print(f"|{'ASSIGNMENTS':^80}|")
    print("-" * 82)
    print(f"|{'Course':<15}{'Assignment Name':<25}{'Due Date':15}{'Status':<10}{'Time Spent':>15}|")
    print("-"*82)

    sorted_report_assignments = sorted(assignmentsDict.values(), key=sortReport)
    for assignment in sorted_report_assignments:
        if assignment['status'] == 'complete':
            print(f"|{assignment['course']:<15}{assignment['name']:<25}{assignment['due']:15}{assignment['status']:<10}{assignment['time']:>15}|")
    print('='*82)

# WORKING MENU
with shelve.open('assignments.shelf') as assignmentsDict:
    while True:
        menu()
        choice = input("Selection: ").strip()
        if choice == '1':
            print()
            viewAssignments()
        elif choice == '2':
            print()
            viewReport()
            assignmentsDict.sync()
        elif choice == '3':
            print()
            addAssignment()
            assignmentsDict.sync()
        elif choice == '4':
            print()
            editAssignment()
            assignmentsDict.sync()
        elif choice == '5':
            print()
            markComplete()
            assignmentsDict.sync()        
        elif choice.upper() == 'X':
            break