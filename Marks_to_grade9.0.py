import pickle

print("=" * 75)
print("MARKS TO GRADE V9.0")
print("=" * 75)

#LOAD EXISTING STUDENTS

names = []
surnames = []
ages = []
marks = []
grades = []
banners = []

try:
    file = open("students.pck", "rb")
    student_data = pickle.load(file)
    file.close()
    
    names = student_data.get('names', [])
    surnames = student_data.get('surnames', [])
    ages = student_data.get('ages', [])
    marks = student_data.get('marks', [])
    grades = student_data.get('grades', [])
    banners = student_data.get('banners', [])
    
    print(f"Loaded {len(names)} students")
    
except:
    print("Starting fresh!")

print()

#FUNCTION DEFINITIONS

def calculation_grade(mark):
    
    if mark < 30:
        return "E"
    elif mark < 40:
        return "D"
    elif mark < 50:
        return "C"
    elif mark < 60:
        return "B2"
    elif mark < 70:
        return "B1"
    elif mark < 80:
        return "A3"
    elif mark < 90:
        return "A2"
    else:
        return "A1"


def view_all_students():
    
    print("\n"+"="*100)
    print("ALL STUDENTS")
    print("="*100)
    
    if len(names) == 0:
        print("No students in database!")
    else:
        for i in range(len(names)):
            print(f"{i + 1}. {names[i]:10} {surnames[i]:10} | Age: {ages[i]:3} | Mark: {marks[i]:5} | Grade: {grades[i]:3} | ID: {banners[i]}")
    print()


def student_exists(banner_id):
    
    for banner in banners:
        if banner.lower() == banner_id.lower():
            return True
    return False


def add_student():
    
    print("\n"+"="*75)
    print("ADD NEW STUDENT")
    print("="*75)
    
    name = input("Student Name:").strip().title()
    surname = input("Student Surname:").strip().title()
    
    # Age validation
    while True:
        try:
            age =int(input("Student Age (0-120):"))
            if age < 0 or age > 120:
                print("Age must be between 0-120!")
                continue
            break
        except ValueError:
            print("Age must be a number!")
    
    # Mark validation
    while True:
        try:
            mark =float(input("Student Mark (0-100):"))
            if mark < 0 or mark > 100:
                print("Mark must be between 0-100!")
                continue
            break
        except ValueError:
            print("Mark must be a number!")
    
    # Calculate grade
    grade = calculation_grade(mark)
    
    # Banner ID with duplicate check
    while True:
        banner_id = input("Student ID:").strip()
        if student_exists(banner_id):
            print(f"Student ID '{banner_id}' already exists!")
            continue
        break
    
    # Add to lists
    names.append(name)
    surnames.append(surname)
    ages.append(age)
    marks.append(mark)
    grades.append(grade)
    banners.append(banner_id)
    
    print(f"{name} {surname} added successfully!")
    print(f"Mark: {mark} | Grade: {grade}")


def delete_student():
    
    if len(names) == 0:
        print("No students to delete!")
        return
    
    print("\n"+"="*75)
    print("DELETE STUDENT")
    print("="*75)
    
    view_all_students()
    
    student_num = int(input("Which student number to delete? >> "))
    
    if 1 <= student_num <= len(names):
        deleted_name = f"{names[student_num - 1]} {surnames[student_num - 1]}"
        
        del names[student_num - 1]
        del surnames[student_num - 1]
        del ages[student_num - 1]
        del marks[student_num - 1]
        del grades[student_num - 1]
        del banners[student_num - 1]
        
        print(f"{deleted_name} deleted!")
    else:
        print(f"Invalid entry! Must be between 1 and {len(names)}")


def search_student():
    
    print("\n"+"="*75)
    print("SEARCH STUDENT")
    print("="*75)
    print("1. Search by Surname")
    print("2. Search by Student ID")
    
    search_choice = input("\nSelect option >> ")
    
    if search_choice == "1":
        search_surname = input("Enter surname: ").strip()
        
        found = False
        for i in range(len(surnames)):
            if surnames[i].lower() == search_surname.lower():
                print("\n"+"=" * 75)
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
            print("No student found with this surname!")
    
    elif search_choice == "2":
        search_id = input("Enter Student ID: ").strip()
        
        found = False
        for i in range(len(banners)):
            if banners[i].lower() == search_id.lower():
                print("\n"+"="*75)
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
            print("No student found with this ID!")
    
    else:
        print("Invalid option!")


def update_student():
    
    if len(names) == 0:
        print("No students to update!")
        return
    
    print("\n"+"="*75)
    print("UPDATE STUDENT MARK")
    print("="*75)
    
    search_id = input("Enter Student ID to update: ").strip()
    
    found = False
    for i in range(len(banners)):
        if banners[i].lower() == search_id.lower():
            print(f"Current: {names[i]} {surnames[i]} | Mark: {marks[i]} | Grade: {grades[i]}")
            
            while True:
                try:
                    new_mark = float(input("Enter NEW mark (0-100): "))
                    if new_mark < 0 or new_mark > 100:
                        print("Mark must be between 0-100!")
                        continue
                    break
                except ValueError:
                    print("Mark must be a number!")
            
            marks[i] = new_mark
            grades[i] = calculation_grade(new_mark)
            
            print(f"Updated! New mark: {new_mark} | New grade: {grades[i]}")
            found = True
            break
    
    if not found:
        print("Student ID not found!")


def view_stats():
    
    if len(names) == 0:
        print("No students for statistics!")
        return
    
    print("\n"+"="*100)
    print("STATISTICS")
    print("="*100)
    
    # Highest mark
    highest_mark = marks[0]
    highest_index = 0
    for i in range(len(marks)):
        if marks[i] > highest_mark:
            highest_mark = marks[i]
            highest_index = i
    
    print(f"HIGHEST: {names[highest_index]} {surnames[highest_index]:15} | {highest_mark:5} marks | Grade {grades[highest_index]}")
    print("-"*100)
    
    # Lowest mark
    lowest_mark = marks[0]
    lowest_index = 0
    for i in range(len(marks)):
        if marks[i] < lowest_mark:
            lowest_mark = marks[i]
            lowest_index = i
    
    print(f"LOWEST:  {names[lowest_index]} {surnames[lowest_index]:15} | {lowest_mark:5} marks | Grade {grades[lowest_index]}")
    print("-"*100)
    
    # Youngest
    youngest_age = ages[0]
    youngest_index = 0
    for i in range(len(ages)):
        if ages[i] < youngest_age:
            youngest_age = ages[i]
            youngest_index = i
    
    print(f"YOUNGEST: {names[youngest_index]} {surnames[youngest_index]:15} | {ages[youngest_index]} years old")
    print("-"*100)
    
    # Eldest
    eldest_age = ages[0]
    eldest_index = 0
    for i in range(len(ages)):
        if ages[i] > eldest_age:
            eldest_age = ages[i]
            eldest_index = i
    
    print(f"ELDEST:   {names[eldest_index]} {surnames[eldest_index]:15} | {ages[eldest_index]} years old")
    print("-" * 100)
    
    # Average
    total_marks = sum(marks)
    average_mark = total_marks / len(marks)
    average_grade = calculation_grade(average_mark)
    
    print(f"AVERAGE:  {average_mark:.1f} marks | Grade {average_grade}")
    print("-" * 100)
    
    # Pass/Fail
    pass_count = sum(1 for mark in marks if mark >= 40)
    fail_count = len(marks) - pass_count
    pass_percent = (pass_count / len(marks)) * 100
    fail_percent = (fail_count / len(marks)) * 100
    
    print(f"PASS (>=40):  {pass_count:2} students ({pass_percent:.1f}%)")
    print(f"FAIL (<40):   {fail_count:2} students ({fail_percent:.1f}%)")
    print("="*100)


def grade_distribution():
   
    if len(names) == 0:
        print("No students for distribution!")
        return
    
    print("\n"+"="*75)
    print("GRADE DISTRIBUTION")
    print("="*75)
    
    # Count each grade
    grade_counts = {}
    for grade in grades:
        grade_counts[grade] = grade_counts.get(grade, 0) + 1
    
    # Display in order
    grade_order = ["A1", "A2", "A3", "B1", "B2", "C", "D", "E"]
    
    for grade in grade_order:
        count = grade_counts.get(grade, 0)
        if count > 0:
            percent = (count / len(grades)) * 100
            bar = "" * count
            print(f"{grade:3}: {bar:20} {count:2} students ({percent:.1f}%)")
    
    print("="*75)


def quit_program():
    
    print("\n"+"="*75)
    print("GOOD BYE!!")
    print("="*75)
    print(f"Database contains {len(names)} student(s)")
    print("="*75)


def invalid_entry():
    
    print(" Invalid ENTRY! Please select 1-9")


def menu():
    
    print("\n"+"="*75)
    print("MAIN MENU")
    print("=" * 75)
    print("1 ADD new student")
    print("2 DELETE student")
    print("3 UPDATE student mark")
    print("4 SEARCH student")
    print("5 VIEW all students")
    print("6 VIEW statistics")
    print("7 GRADE distribution")
    print("8 QUIT and save")
    
    choice = input("Option >>> ")
    return choice

#MAIN PROGRAM

menu_option = menu()

while True:
    
    if menu_option == "1":
        add_student()
    
    elif menu_option == "2":
        delete_student()
    
    elif menu_option == "3":
        update_student()
    
    elif menu_option == "4":
        search_student()
    
    elif menu_option == "5":
        view_all_students()
    
    elif menu_option == "6":
        view_stats()
    
    elif menu_option == "7":
        grade_distribution()
    
    elif menu_option == "8":
        quit_program()
        break
    
    else:
        invalid_entry()
    
    menu_option = menu()

#SAVE DATA

print("Saving student database...")

student_data = {
    'names': names,
    'surnames': surnames,
    'ages': ages,
    'marks': marks,
    'grades': grades,
    'banners': banners
}

file = open("students.pck", "wb")
pickle.dump(student_data, file)
file.close()

print("All student data saved to students.pck")
print("Goodbye!")
