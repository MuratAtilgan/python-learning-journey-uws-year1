print("Mark to Grade Level7")


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
ages = []
marks = []
grades = []
banners = []

for i in range(student_count):
    print(f"\n ***STUDENT {i + 1}***")

    name = input("Student Name:\t")
    names.append(name)

    age = int(input("Student Age:\t"))
    while age < 18 or age > 120:
        print("Invalid age!! Age must be between 18-120")      #age gaps validation 
        age = int(input("Student Age:"))
    ages.append(age)

    mark = float(input("Student Mark:\t"))     #made here float just in case result has decimal numbers
    while mark < 0 or mark > 100:
        print("Invalid entry!! Mark must be between 0-100")   #mark gaps validation 
        mark = float(input("Student Mark:"))
    marks.append(mark)

    grade = calculation_grade(mark)
    grades.append(grade)

    bannerid = input("Student ID:\t")       #added new selection which is banner id
    banners.append(bannerid)

    print("="*100)
    print(f"|{name}| |{age} years old| | Marks:{mark}-Grade:{grade}|Student ID: {bannerid}|")
    print("="*100)


print("ALL STUDENTS")
print("="*100)


for i in range(student_count):
    print(
        f"{i + 1}. {names[i]:20} | Age: {ages[i]:4} | Mark: {marks[i]:5} | Grade: {grades[i]}|Student ID:{banners[i]}") #added option to limit characters
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

print(f"|HIGHEST MARK: {names[highest_mark_student]}| with |{highest_mark} marks| |Grade {grades[highest_mark_student]}|")
print("-"*75)
lowest_mark=marks[0]
lowest_mark_student=0
for i in range(len(marks)):
    if marks[i]<lowest_mark:
        lowest_mark=marks[i]
        lowest_mark_student=i

print(f"|LOWEST MARK: {names[lowest_mark_student]}| with |{lowest_mark} marks| |Grade {grades[lowest_mark_student]}|")
print("-"*75)
youngest_age=ages[0]
youngest_student=0
for i in range(len(ages)):
    if ages[i]<youngest_age:
        youngest_age=ages[i]
        youngest_student=i

print(f"|YOUNGEST STUDENT is {names[youngest_student]}| at |{ages[youngest_student]} years old|")
print("-"*75)
eldest_age=ages[0]
eldest_student=0
for i in range(len(ages)):
    if ages[i] > eldest_age:
        eldest_age=ages[i]
        eldest_student=i

print(f"|ELDEST STUDENT is {names[eldest_student]}| at |{ages[eldest_student]} years old|")
print("-"*75)
total_marks=0
for mark in marks:
    total_marks +=mark
average_marks=total_marks/student_count
average_grade=calculation_grade(average_marks)

print(f"|AVERAGE MARK is {average_marks:.1f}| and |GRADE {average_grade}| ")
print("*"*75)

print("Thanks for watching us and see you at level8")




