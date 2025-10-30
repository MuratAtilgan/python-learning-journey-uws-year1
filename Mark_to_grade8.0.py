print("Mark to Grade Level7.5")


def calculation_grade(mark):
    if mark < 30:
        gradex = "E"
    elif mark < 40:
        gradex = "D"
    elif mark < 50:
        gradex = "C"
    elif mark < 60:
        gradex = "B2"
    elif mark < 70:
        gradex = "B1"
    elif mark < 80:
        gradex = "A3"
    elif mark < 90:
        gradex = "A2"
    else:
        gradex = "A1"
    return gradex


print("=" * 75)
print("Level 7")
print("=" * 75)

student_count = int(input("How many student do you want to assess?"))

names = []
surnames=[]
ages = []
marks = []
grades = []
banners = []

for i in range(student_count):
    print(f"\n ***STUDENT {i + 1}***")

    name = input("Student Name:\t")
    names.append(name)

    surname=input("Student Surname:\t")
    surnames.append(surname)

    while True:
        try:
            age=int(input("Student Age (0-120):\t"))
            if age < 0 or age >120:
                print("Invalid entry! Age must be between 0-120")
                continue
            break
        except ValueError:
            print("Invalid entry! Must a number")   #character validation for age
    ages.append(age)

    while True:
        try:
            mark = float(input("Student Mark (0-100): "))
            if mark < 0 or mark > 100:
                print("Invalid entry!! Mark must be between 0-100")
                continue
            break
        except ValueError:
            print("Invalid entry!! Mark must be a number")      #character validation for mark
    marks.append(mark)

    grade = calculation_grade(mark)
    grades.append(grade)

    bannerid = input("Student ID:\t")       #added new selection which is banner id
    banners.append(bannerid)

    print("="*100)
    print(f"|{name} {surname} |{age} years old| | Marks:{mark}-Grade:{grade}|Student ID: {bannerid}|")
    print("="*100)


print("ALL STUDENTS")
print("="*100)


for i in range(student_count):
    print(
        f"{i + 1}. {names[i]:10} {surnames[i]:10}| Age: {ages[i]:4} | Mark: {marks[i]:5} | Grade: {grades[i]}|Student ID:{banners[i]}") #added option to limit characters
              # names[i]:15 -means allow user to enter 15 characters including-keyboard
print("*"*100)
print("STATS")
print("*"*100)



highest_mark=marks[0]
highest_mark_student=0
for i in range(len(marks)):
    if marks[i] > highest_mark:
        highest_mark=marks[i]
        highest_mark_student=i

print(f"|HIGHEST MARK: {names[highest_mark_student]} {surnames[highest_mark_student]:20}| with |{highest_mark:5} marks| |Grade {grades[highest_mark_student]:5}|")
print("-"*75)
lowest_mark=marks[0]
lowest_mark_student=0
for i in range(len(marks)):
    if marks[i]<lowest_mark:
        lowest_mark=marks[i]
        lowest_mark_student=i

print(f"|LOWEST MARK: {names[lowest_mark_student]} {surnames[lowest_mark_student]:20}| with |{lowest_mark:5} marks| |Grade {grades[lowest_mark_student]:5}|")
print("-"*75)
youngest_age=ages[0]
youngest_student=0
for i in range(len(ages)):
    if ages[i]<youngest_age:
        youngest_age=ages[i]
        youngest_student=i

print(f"|YOUNGEST STUDENT is {names[youngest_student]} {surnames[youngest_student]:20}| at |{ages[youngest_student]:5} years old|")
print("-"*75)
eldest_age=ages[0]
eldest_student=0
for i in range(len(ages)):
    if ages[i] > eldest_age:
        eldest_age=ages[i]
        eldest_student=i

print(f"|ELDEST STUDENT is {names[eldest_student]} {surnames[eldest_student]:20}| at |{ages[eldest_student]:5} years old|")
print("-"*75)
total_marks=0
for mark in marks:
    total_marks +=mark
average_marks=total_marks/student_count
average_grade=calculation_grade(average_marks)

print(f"|AVERAGE MARK is {average_marks:.1f}| and |GRADE {average_grade}| ")

print("="*75)
print("SAVING STUDENT DATA")
print("="*75)

student_data = {        #we store student data for following versions and enhanced models of this
    'names': names,
    'surnames': surnames,
    'ages': ages,
    'marks': marks,
    'grades': grades,
    'banners': banners
}

data_file = open("students.pck", "wb")
pickle.dump(student_data, data_file)
data_file.close()

print("All student data saved to students.pck")
print("="*75)

print("Thanks for watching us and see you at level8")

# SEARCH MENU
while True:
    print("\n" + "="*75)
    print("SEARCH MENU")
    print("="*75)
    print("1. Search by Surname")
    print("2. Search by Student ID")
    print("3. Exit")
    
    search_choice = int(input("\nSelect option >> "))
    
    if search_choice == 1:
        
        search_surname = input("Enter surname to search: ").strip() # SEARCH BY SURNAME
        
        found = False
        for i in range(len(surnames)):
            if surnames[i] == search_surname:  # Exact match!
                print("\n" + "="*75)
                print("STUDENT FOUND!")
                print("="*75)
                print(f"Name: {names[i]} {surnames[i]}")
                print(f"Age: {ages[i]} years old")
                print(f"Mark: {marks[i]}")
                print(f"Grade: {grades[i]}")
                print(f"Student ID: {banners[i]}")
                print("="*75)
                found = True
                break  # Stop after first match
        
        if not found:
            print("No student found with that surname!")
    
    elif search_choice == 2:
        
        search_id = input("Enter Student ID to search: ").strip()  # SEARCH BY BANNER ID
        
        found = False
        for i in range(len(banners)):
            if banners[i] == search_id:  # Exact match!
                print("\n" + "="*75)
                print("STUDENT FOUND!")
                print("="*75)
                print(f"Name: {names[i]} {surnames[i]}")
                print(f"Age: {ages[i]} years old")
                print(f"Mark: {marks[i]}")
                print(f"Grade: {grades[i]}")
                print(f"Student ID: {banners[i]}")
                print("="*75)
                found = True
                break
        
        if not found:
            print("No student found with that ID!")
    
    elif search_choice == 3:
        print("Goodbye!")
        break
    
    else:
        print("Invalid Entry!")