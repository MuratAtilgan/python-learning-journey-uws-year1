#Week7 Menu

print("Please select one of the following")
print("Type A below if you want to ADD")
print("Type S below if you want to SUBTRACT")
print("Type M below if you want to MULTIPLY")
print("Type D below if you want to DIVIDE")

menu_choice=input(">>")

number1=int(input("Enter the first number >>"))
number2=int(input("Enter the second number >>"))

if menu_choice == "A":
    answer=number1+number2
    print(f"If you ADD {number1} to {number2} you get {answer}")
elif menu_choice =="S":
    answer=number1-number2
    print(f"if you SUBTRACT {number2} from {number1} you get {answer}")
elif menu_choice == "M":
    answer=number1*number2
    print(f"if you MULTIPLY {number1} by {number2} you get {answer}")
elif menu_choice == "D":
    answer=number1/number2 
    print(f"if you DIVIDE {number1} by {number2} you get {answer}" )

#Validation

print("Please select one of the following")
print("Type A below if you want to ADD")
print("Type S below if you want to SUBTRACT")
print("Type M below if you want to MULTIPLY")
print("Type D below if you want to DIVIDE")

menu_choice=input(">>")

number1=int(input("Enter the first number >>"))
number2=int(input("Enter the second number >>"))

if menu_choice == "A":
    answer=number1+number2
    print(f"If you ADD {number1} to {number2} you get {answer}")
elif menu_choice =="S":
    answer=number1-number2
    print(f"if you SUBTRACT {number2} from {number1} you get {answer}")
elif menu_choice == "M":
    answer=number1*number2
    print(f"if you MULTIPLY {number1} by {number2} you get {answer}")
elif menu_choice == "D":
    if number2 ==0:
       print("Sorry,You can't divide by 0")        #program print this out and stucks there so not enough
    else:
       answer=number1/number2
       print(f"if you DIVIDE {number1} by {number2} you get {answer}" )


#Validation
print("Please select one of the following")
print("Type A below if you want to ADD")
print("Type S below if you want to SUBTRACT")
print("Type M below if you want to MULTIPLY")
print("Type D below if you want to DIVIDE")

menu_choice=input(">>")   #even choosing different letters it will still let to choice numbers and then will say "invalid entry"

number1=int(input("Enter the first number >>"))  
number2=int(input("Enter the second number >>"))

if menu_choice == "A":
    answer=number1+number2
    print(f"If you ADD {number1} to {number2} you get {answer}")
elif menu_choice =="S":
    answer=number1-number2
    print(f"if you SUBTRACT {number2} from {number1} you get {answer}")
elif menu_choice == "M":
    answer=number1*number2
    print(f"if you MULTIPLY {number1} by {number2} you get {answer}")
elif menu_choice == "D":
    if number2 ==0:
       print("Sorry,You can't divide by 0")
    else:
       answer=number1/number2
       print(f"if you DIVIDE {number1} by {number2} you get {answer}" )
else:
    print("Invalid Entry")


#Upper & Lower case sensivity  
             
print("Please select one of the following")
print("Type A below if you want to ADD")
print("Type S below if you want to SUBTRACT")
print("Type M below if you want to MULTIPLY")
print("Type D below if you want to DIVIDE")

menu_choice=input(">>").upper()   #when we add this it will still work regardless of upper or lower case .upper() capitalize all letters.

number1=int(input("Enter the first number >>"))  
number2=int(input("Enter the second number >>"))

if menu_choice == "A":
    answer=number1+number2
    print(f"If you ADD {number1} to {number2} you get {answer}")
elif menu_choice =="S":
    answer=number1-number2
    print(f"if you SUBTRACT {number2} from {number1} you get {answer}")
elif menu_choice == "M":
    answer=number1*number2
    print(f"if you MULTIPLY {number1} by {number2} you get {answer}")
elif menu_choice == "D":
    if number2 ==0:
       print("Sorry,You can't divide by 0")
    else:
       answer=number1/number2
       print(f"if you DIVIDE {number1} by {number2} you get {answer}" )
else:
    print("Invalid Entry")  

#Logical Operators- and operator

number1=int(input("Num1?   >"))
number2=int(input("Num2?   >"))
number3=int(input("Num3?   >"))
number4=int(input("Num4?   >"))

print()

print(f"Condition1: {number1}<{number2} is {number1<number2}")
print(f"Condition2: {number3}<{number4} is {number3<number4}")

if (number1<number2) and (number3<number4):
    print("Both conditions are TRUE")
else:
    print("At least one conditions is FALSE")

#Logical Operators- or operator

number1=int(input("Num1?   >"))
number2=int(input("Num2?   >"))
number3=int(input("Num3?   >"))
number4=int(input("Num4?   >"))

print()

print(f"Condition1: {number1}<{number2} is {number1<number2}")
print(f"Condition2: {number3}<{number4} is {number3<number4}")

if (number1<number2) or (number3<number4):
    print("At least one conditions is True")
else:
    print("Both conditions are FALSE")


#Logical Operators- the "not" operator

num=int(input("Please enter a number less than 7 >"))

if not(num<7):
    print(f"Seriously?{num} is less than 7?")
else:
    print("Oh well done!")

num=int(input("Please enter a number less than 7 >"))

if not(num<7):
    print(f"Seriously?{num} is less than 7?")
else:
    print("Oh well done!")

#Long version of case sensivity

print("Please select one of the following")
print("Type A below if you want to ADD")
print("Type S below if you want to SUBTRACT")
print("Type M below if you want to MULTIPLY")
print("Type D below if you want to DIVIDE")

menu_choice=input(">>")   

number1=int(input("Enter the first number >>"))  
number2=int(input("Enter the second number >>"))

if menu_choice == "A" or menu_choice == "a":
    answer=number1+number2
    print(f"If you ADD {number1} to {number2} you get {answer}")
elif menu_choice =="S" or menu_choice == "s":
    answer=number1-number2
    print(f"if you SUBTRACT {number2} from {number1} you get {answer}")
elif menu_choice == "M" or menu_choice == "m":
    answer=number1*number2
    print(f"if you MULTIPLY {number1} by {number2} you get {answer}")
elif menu_choice == "D" or menu_choice == "d":
    if number2 ==0:
       print("Sorry,You can't divide by 0")
    else:
       answer=number1/number2
       print(f"if you DIVIDE {number1} by {number2} you get {answer}" )
else:
    print("Invalid Entry")


#Exercise- Zen of Python

print("="*75)
print()
print("ZEN OF PYTHON-Tim Peters")
print()
print("Please  choose one of the principles of Zen of Python ")
print("Type B for the first principle")
print("Type E for the second principle")
print("Type S for the third principle")
print("Type C for the fourth principle")
print("Type F for the fifth principle")
print("Type R for the sixth principle")

menu_choice=input(">>").upper().strip()  #- .strip()-only for string prevents "invalid entry" just in case user press space on keyboard 

if menu_choice == "B":
    print("1 Beautiful is better than ugly. ")
elif menu_choice == "E":
    print("2  Explicit is better than implicit. ")
elif menu_choice == "S":
    print("3  Simple is better than complex. ")
elif menu_choice == "C":
    print("4  Complex is better than complicated. ")
elif menu_choice == "F":
    print("5  Flat is better than nested. ")
elif menu_choice == "R":
    print("6  Readability counts. ")
else:
    print("Invalid entry")


#Lab Question 1

print("Please select one of the following")   #printing about program 
print("Type A if you want to ADD")
print("Type S if you want to SUBTRACT")
print("Type M if you want to MULTIPLY")
print("Type D if you want to DIVIDE")

menu_choice=input(">>") #asking to choose an option from menu
num1=int(input("Please enter a number")) #first number choice
num2=int(input("Please enter another number")) #second number choice

if menu_choice == "A":
    answer=num1+num2 #calculation of selection
    print(f"if you add {num1} and {num2} then you get {answer}") #printing result of calculation
elif menu_choice == "S":
    answer=num1-num2
    print(f"if you subtract {num2} from {num1} you get {answer}")
elif menu_choice == "M":
    answer=num1*num2
    print(f"if you multiply {num1} by {num2} you get {answer}")
elif menu_choice == "D":
    answer=num1/num2
    print(f"if you devide {num1} by {num2} you get {answer}")
else:
    print("Invalid Entry")   #when make an entry apart from mentioned above A,S,M,D


# I want to make program more user friendly just incase of a wrong entry 

print("Please select one of the following")   
print("Type A if you want to ADD")
print("Type S if you want to SUBTRACT")
print("Type M if you want to MULTIPLY")
print("Type D if you want to DIVIDE")

menu_choice=input(">>") #asking to choose an option from menu

while menu_choice != ["A","S","M","D"]: #made a list to make choice
    print("Invalid entry")
    break #break the program 
print("Menu contains= A,S,M,D letters only enter a valid choice:") #remind what is valid
menu_choice=input(">>") #again asked same as above 

num1=int(input("Please enter a number")) #first number choice
num2=int(input("Please enter another number")) #second number choice

if menu_choice == "A":
    answer=num1+num2 #calculation of selection
    print(f"if you add {num1} and {num2} then you get {answer}") #printing result of calculation
elif menu_choice == "S":
    answer=num1-num2
    print(f"if you subtract {num2} from {num1} you get {answer}")
elif menu_choice == "M":
    answer=num1*num2
    print(f"if you multiply {num1} by {num2} you get {answer}")
elif menu_choice == "D":
    answer=num1/num2
    print(f"if you devide {num1} by {num2} you get {answer}")
#else: print("we dont need "else:" anymmore here as we have added a validation above") 

#Lab Question 2
#adding modulus, Floor Division and Exponentiation

print("Please select one of the following")   
print("Type A if you want to ADD")
print("Type S if you want to SUBTRACT")
print("Type M if you want to MULTIPLY")
print("Type D if you want to DIVIDE")
print("Type MD if you want to MODULUS") #adding modulus 
print("Type F if you want to FLOOR division") # adding floor division
print("Type E if you want to EXPONENTIATION") #adding exponentiation

menu_choice=input(">>")

num1=int(input("enter your first number"))
num2=int(input("enter your second number"))

if menu_choice == "A":
    answer=num1+num2 
    print(f"if you add {num1} and {num2} then you get {answer}") 
elif menu_choice == "S":
    answer=num1-num2
    print(f"if you subtract {num2} from {num1} you get {answer}")
elif menu_choice == "M":
    answer=num1*num2
    print(f"if you multiply {num1} by {num2} you get {answer}")
elif menu_choice == "D":
    answer=num1/num2
    print(f"if you devide {num1} by {num2} you get {answer}") 
elif menu_choice  == "MD": 
    answer=num1%num2        #remaining whole number after division 
    print(f"if you modulus {num1} by {num2} you get {answer}")
elif menu_choice == "F":
    answer=num1//num2    #flooring down to whole number after division
    print(f"if you floor {num1} by {num2} you get {answer}")
elif menu_choice == "E":
    answer=num1**num2   #powering up to first number by num2 times 
    print(f"if you exponentiate {num1} by {num2} you get {answer}")
else:
    print("Invalid Entry")

#Lets put more validation 

print("Please select one of the following")   
print("Type A if you want to ADD")
print("Type S if you want to SUBTRACT")
print("Type M if you want to MULTIPLY")
print("Type D if you want to DIVIDE")
print("Type MD if you want to MODULUS") #adding modulus 
print("Type F if you want to FLOOR division") # adding floor division
print("Type E if you want to EXPONENTIATION") #adding exponentiation

menu_choice=input(">>")

while menu_choice != ["A","S","M","D","MD","F","E"]: 
    print("Invalid entry")
    break 
print("Menu contains: A,S,M,D,MD,F,E letters only enter a valid choice:") 
menu_choice=input(">>") 

num1=int(input("enter your first number"))
num2=int(input("enter your second number"))

if menu_choice == "A":
    answer=num1+num2 
    print(f"if you add {num1} and {num2} then you get {answer}") 
elif menu_choice == "S":
    answer=num1-num2
    print(f"if you subtract {num2} from {num1} you get {answer}")
elif menu_choice == "M":
    answer=num1*num2
    print(f"if you multiply {num1} by {num2} you get {answer}")
elif menu_choice == "D":
    answer=num1/num2
    print(f"if you devide {num1} by {num2} you get {answer}") 
elif menu_choice  == "MD": 
    answer=num1%num2        #remaining whole number after division 
    print(f"if you modulus {num1} by {num2} you get {answer}")
elif menu_choice == "F":
    answer=num1//num2    #flooring down to whole number after division
    print(f"if you floor {num1} by {num2} you get {answer}")
elif menu_choice == "E":
    answer=num1**num2   #powering up to first number by num2 times 
    print(f"if you exponentiate {num1} by {num2} you get {answer}")

#Lab Question 3

print("="*75)
print()
print("ZEN OF PYTHON-Tim Peters")
print()
print("Please  choose one of the principles of Zen of Python ")
print("Type B for the first principle")
print("Type E for the second principle")
print("Type S for the third principle")
print("Type C for the fourth principle")
print("Type F for the fifth principle")
print("Type R for the sixth principle")

menu_choice=input(">>").upper().strip()  #- .strip() prevents "invalid entry" just in case user press space on keyboard 

pr_1="Beautiful is better than ugly."
pr_2="Explicit is better than implicit."
pr_3="Simple is better than complex."
pr_4="Complex is better than complicated."
pr_5="Flat is better than nested."
pr_6="Readability counts."

if menu_choice == "B":
    print(f" 1-) {pr_1}")
elif menu_choice == "E":
    print(f" 2-) {pr_2}")
elif menu_choice == "S":
    print(f" 3-) {pr_3}")
elif menu_choice == "C":
    print(f" 4-) {pr_4}")
elif menu_choice == "F":
    print(f" 5-) {pr_5}")
elif menu_choice == "R":
    print(f" 6-) {pr_6}")
else:
    print("Invalid entry")


#Lab Question 4

print("="*75)
print()
print("MONTY PYTHON TEAM-6 members")
print()

print("Please  choose one of the member  of Monty Python ")
print("Type 1 for the first member")
print("Type 2 for the second member")
print("Type 3 for the third member")
print("Type 4 for the fourth member")
print("Type 5 for the fifth member")
print("Type 6 for the sixth member")

monty_python=int(input("Select the member "))

member1="Graham Chapman,Born:January 8, 1941, in Leicester, England."
member2="John Cleese,Born: October 27, 1939, in Weston-super-Mare, Somerset, England."
member3="Eric Idle,Born: March 29, 1943, in South Shields, Tyne and Wear, England."
member4="Terry Jones,Born: February 1, 1942, in Colwyn Bay, Denbighshire, Wales."
member5="Michael Palin,Born: May 5, 1943, in Sheffield, Yorkshire, England."
member6="Terry Gilliam,Born: November 22, 1940, in Minneapolis, Minnesota, United States."

if monty_python == 1:
    print(f"You selected {member1}")
elif monty_python == 2:
    print(f"You selected {member2}")
elif monty_python == 3:
    print(f"You selected {member3}")
elif monty_python == 4:
    print(f"You selected {member4}")
elif monty_python == 5:
    print(f"You selected {member5}")
elif monty_python == 6:
    print(f"You selected {member6}")
else:
    print("YOU SELECTED ME and I AM NOT A MEMBER OF MONTY PYTHON ")

#Mark_to_Grade version7.0

print("Mark to Grade Version7.0")


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

print("Thanks for watching us and see you at Version7.5")

#Mark_to_Grade version7.5

print("Mark to Grade Version7.5")


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
print("Level 7.5")
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
print("*"*75)

print("Thanks for watching us and see you at Version8.0")


