#Week5 Exercises
#Nested for loops

for i in range(1,5):
    for j in range(1,9):
        print(i*j,"\t",end="")
    print()    

#While Loops
#Example1
number = int(input("Enter a number (0 to stop): "))

while number != 0:
    print("You entered:", number)
    number = int(input("Enter another number (0 to stop): "))

print("Loop ended because you entered 0.")

#Example 2

total=0
number=float(input("Enter the first number(or 0 to quit)..."))
while (number !=0):
    total=total+number
    number=float(input("Enter the first number(or 0 to quit)..."))
print("The total is",total)

# Example 3: Finding the largest number entered

largest = None
number = float(input("Enter a number (-1 to finish): "))

while number != -1:
    if largest is None or number > largest:
        largest = number
    number = float(input("Enter another number (-1 to finish): "))

if largest is not None:
    print("The largest number entered was:", largest)
else:
    print("No numbers were entered.")

# Example 4 Run at least once :):)

while True:
    number=float(input("Enter the first number(or 0 to quit)..."))
    print("You entered",number)
    if number ==0:
        break
print("All done!!!") 

#Example 5

while True:
    number = float(input("Enter a number (0 to stop): "))
    print("You entered:", number)
    
    if number == 0:
        break

print("Completed.")

#Example 6 "Counter" 

counter=0
while counter <5:
    print("counter=",counter)
    counter+=1

#Example 7 Use one of the loops to amend the Marks to Grades program to allow you to enter five students’ marks.

print("Assessment RESULTS")

student = 0  

while student < 5:  
    student_result = int(input("What is the mark of the student? "))

    if student_result < 30:
        result = "E"
    elif student_result < 40:
        result = "D"
    elif student_result < 50:
        result = "C"    
    elif student_result < 60:
        result = "B2"
    elif student_result < 70:
        result = "B1"
    elif student_result < 80:
        result = "A3"    
    elif student_result < 90:
        result = "A2"    
    else: 
        result = "A1"    

    print("Assessment result for this student is GRADE", result)

    student += 1 

#program is asking "How many students"

print("="*50)    # this is print seperator  and can use different version of it for example print("="*30),print("-"*75)
print("ASSESSMENT RESULTS")
print("="*50)

student_count=int(input("How many students do you want to assess?"))

print("="*50)

student=0

while student < student_count:

    student_result = int(input(f"What is the mark of student {student + 1} ?"))  # student+1 = shows how manyth student for example student 1 
                                                                                 #we use f string as we wanna convert int to str - 
    if student_result < 30:                                                      #F-strings automatically convert numbers (like int, float) into strings when you put them inside {}
        result = "E"
    elif student_result < 40:
        result = "D"
    elif student_result < 50:
        result = "C"    
    elif student_result < 60:
        result = "B2"
    elif student_result < 70:
        result = "B1"
    elif student_result < 80:
        result = "A3"    
    elif student_result < 90:
        result = "A2"    
    else: 
        result = "A1" 

    print(f"student{student+1}:{student_result} marks - GRADE{result}")  #student+1 = how manyth student   student_result=mark   result= grade 
    print("="*50)

    student +=1    

#time to enhance it and  get average result of marks and their average grade also invalid number check

print("=" * 50)
print("Assessment RESULTS")
print("=" * 50)


student_count = int(input("How many students do you want to assess? "))
print("=" * 50)

student = 0  
total_marks = 0  

while student < student_count:  
    student_result = int(input(f"What is the mark of student {student + 1}? "))
    
    while student_result < 0 or student_result > 100:
        print("Invalid! Mark must be between 0 and 100.")
        student_result = int(input(f"What is the mark of student {student + 1}? "))
    
    total_marks += student_result  

    
    if student_result < 30:
        result = "E"
    elif student_result < 40:
        result = "D"
    elif student_result < 50:
        result = "C"    
    elif student_result < 60:
        result = "B2"
    elif student_result < 70:
        result = "B1"
    elif student_result < 80:
        result = "A3"    
    elif student_result < 90:
        result = "A2"    
    else: 
        result = "A1"    

    print(f"Student {student + 1}: {student_result} marks - GRADE {result}")      #student(0+1) student(1+1)....
    print("-" * 50)

    student += 1


average_mark = total_marks / student_count


if average_mark < 30:
    avg_grade = "E"
elif average_mark < 40:
    avg_grade = "D"
elif average_mark < 50:        # DRY - do not repeat yourself .... 
    avg_grade = "C"    
elif average_mark < 60:
    avg_grade = "B2"
elif average_mark < 70:
    avg_grade = "B1"
elif average_mark < 80:
    avg_grade = "A3"    
elif average_mark < 90:
    avg_grade = "A2"    
else: 
    avg_grade = "A1"

# Display -showtime:)
print("=" * 50)
print("CLASS SUMMARY")
print("=" * 50)
print(f"Total students assessed: {student_count}")
print(f"Average mark: {average_mark}")      #we could add "":.1f"  to average_mark as it keep 1 decimal place
print(f"Average grade: {avg_grade}")
print("=" * 50)


#To be able to see highest and lowest mark by just adding an another condition 

print("=" * 50)
print("Assessment RESULTS")
print("=" * 50)


student_count = int(input("How many students do you want to assess? "))
print("=" * 50)

student = 0  
total_marks = 0  

while student < student_count:  
    student_result = int(input(f"What is the mark of student {student + 1}? "))
    
    while student_result < 0 or student_result > 100:
        print("Invalid! Mark must be between 0 and 100.")
        student_result = int(input(f"What is the mark of student {student + 1}? "))
    
    total_marks += student_result  

    
    if student_result < 30:
        result = "E"
    elif student_result < 40:
        result = "D"
    elif student_result < 50:
        result = "C"    
    elif student_result < 60:
        result = "B2"
    elif student_result < 70:
        result = "B1"
    elif student_result < 80:
        result = "A3"    
    elif student_result < 90:
        result = "A2"    
    else: 
        result = "A1"    

    print(f"Student {student + 1}: {student_result} marks - GRADE {result}")
    print("-" * 50)

    student += 1


average_mark = total_marks / student_count


if average_mark < 30:
    avg_grade = "E"
elif average_mark < 40:
    avg_grade = "D"
elif average_mark < 50:        # DRY - do not repeat yourself .... 
    avg_grade = "C"    
elif average_mark < 60:
    avg_grade = "B2"
elif average_mark < 70:
    avg_grade = "B1"
elif average_mark < 80:
    avg_grade = "A3"    
elif average_mark < 90:
    avg_grade = "A2"    
else: 
    avg_grade = "A1"

# Display -showtime:)
print("=" * 50)
print("CLASS SUMMARY")
print("=" * 50)
print(f"Total students assessed: {student_count}")
print(f"Average mark: {average_mark}")      #we could add "":.1f"  to average_mark as it keep 1 decimal place
print(f"Average grade: {avg_grade}")
print("=" * 50)


#to be able to see highest and lowest results by adding another condition and variables

print("=" * 50)
print("Assessment RESULTS")
print("=" * 50)


student_count = int(input("How many students do you want to assess? "))
print("=" * 50)

student = 0  
total_marks = 0  

highest_mark =None
lowest_mark =None


while student < student_count:  
    student_result = int(input(f"What is the mark of student {student + 1}? "))
    
    while student_result not in range(1,101):           #student_result < 0 or student_result >  alternative way
        print("Invalid! Mark must be between 0 and 100.")
        student_result = int(input(f"What is the mark of student {student + 1}? "))
    
    total_marks += student_result  
    
    if highest_mark == None:
       highest_mark=student_result
       lowest_mark=student_result
    else:
        if student_result>highest_mark:
           highest_mark=student_result
        if student_result<lowest_mark:
           lowest_mark=student_result

    
    if student_result < 30:
        result = "E"
    elif student_result < 40:
        result = "D"
    elif student_result < 50:
        result = "C"    
    elif student_result < 60:
        result = "B2"
    elif student_result < 70:
        result = "B1"
    elif student_result < 80:
        result = "A3"    
    elif student_result < 90:
        result = "A2"    
    else: 
        result = "A1"    

    print(f"Student {student + 1}: {student_result} marks - GRADE {result}")
    print("-" * 50)

    student += 1


average_mark = total_marks / student_count


if average_mark < 30:
    avg_grade = "E"
elif average_mark < 40:
    avg_grade = "D"
elif average_mark < 50:
    avg_grade = "C"    
elif average_mark < 60:
    avg_grade = "B2"
elif average_mark < 70:
    avg_grade = "B1"
elif average_mark < 80:
    avg_grade = "A3"    
elif average_mark < 90:
    avg_grade = "A2"    
else: 
    avg_grade = "A1"

# Display -showtime:)
print("=" * 50)
print("CLASS SUMMARY")
print("=" * 50)
print(f"Total students assessed: {student_count}")
print(f"Average mark: {average_mark}")
print(f"Average grade: {avg_grade}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark:{lowest_mark}")
print("=" * 50)

#Lab5 Question 1  multiplication table

rows = range(11, 2, -4)   

columns = range(2, 17, 2)

print("X", end="\t")   # Top-left corner of multiplication table
for col in columns:
    print(col, end="\t")  # print columns=range(2,17,2) beside "x"
print()

for row in rows:
    print(row, end="\t")  # print rows = range(11, 2, -4)

    for col in columns:
        print(row * col, end="\t") 
    
    print()  # New line after each row

print("-"*100)  
    

#similar exercise for practising purpose this time we want to make  an addition table  

number_of_pen =range(25,1,-2)

number_of_paper = range(1,19,2)

print("Y", end="\t")
for paper in number_of_paper:
    print(paper, end="\t")
print()

for pen in number_of_pen:
    print(pen,end="\t")
    
    for paper in number_of_paper:
        print(pen+paper,end="\t")
    print()

#Lab5 Question2  No two people have the same name.

print("-"*68)
print("INHABITANT OF THE VILLAGE")
print("-"*68)

surnames=['McIntosh','McGregor','McDonald','McKenzie']        #this is a 4x4 combo = 16 
first_names=['Angus','Hamish','Morag','Mhairi']               # total_combination=(list1xlist2xlist3.................xlistn)

for name in first_names:
    for surname in surnames:     #runs 4 times for each first name
        print(name,surname)

print("="*75)
print("WELCOME TO OUR VILLAGE")
print("="*75)

#will enhance this with a travel example -triple nested loops

print("-"*75)
print("NEVADA ITENARY ")
print("-"*75)

cities=['Las Vegas','Carson City','Reno']
hotels=['Hotel A','Hotel B','Hotel C']
dates=['16 September 2026','18 September 2026','21 September 2026'] #"The algorithm is independent of the data type!"
                                                                    
for city in cities:                                                 #polymorphism- one pattern,many data types :):)
    for hotel in hotels:
        for date in dates:
            print(f"{date} {city} {hotel}")

print("="*100)
print("HAVE A GOOD TIME")
print("="*100)

#Lab5 Question 3

import random

print("="*100)
print("GUESS WHAT")
print("="*100)

secret_number=random.randrange(1,101)    # we could also use randint(1,100)
guess_count=0

number = 0

while number !=secret_number:
      number=int(input("Please guess a number between 1-100"))
      guess_count +=1

      if number < secret_number:
            result="TOO LOW"
      elif number > secret_number:
            result="TOO HIGH"
      else:
            result="CORRECT"

      print(result)

print("="*100)
print("CONGRATULATIONS !!")
print(f"You found the correct number in {guess_count} guesses")  
print("="*100)    

#again to enhance it by limiting guessing time.

import random

print("="*100)
print("GUESS WHAT")
print("="*100)

max_guess_time=10
print(f"You have {max_guess_time} guess to find correct number")
print("=")

secret_number=random.randrange(1,101)    # we could also use randint(1,100)
guess_count=0

number = 0

while guess_count < max_guess_time:
      number=int(input("Please guess a number between 1-100"))

      while number not in range(1,101):
            print("Invalid number!! Choose between 1-100")
            number=int(input("Please guess a number between 1-100"))

      guess_count +=1

      if number < secret_number:
            result="TOO LOW"
      elif number > secret_number:
            result="TOO HIGH"
      else:
            result="CORRECT"
            break                     # while studying_hard:
      print(result)                          #if exhausted:
                                                 #break          need a wee break :):
print("="*100)

if number == secret_number:
   print("CONGRATULATIONS !!")
   print(f"You found the correct number in {guess_count} guesses")  
else:
   print(f"Out of guess!! Correct number is{secret_number}")   

print("="*100)    


# name,marks,grade and age and showing youngest,eldest,highest and lowest 

def calculate_grade(mark):
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



print("=" * 75)
print("Enhanced Version")
print("=" * 75)


student_count = int(input("How many students do you want to assess? "))
print("=" * 75)


names = []                         #  lists to store student data
ages = []
marks = []
grades = []


for i in range(student_count):                     # Collect data for each student
    print(f"\n--- STUDENT {i + 1} ---")

    # Get name
    name = input("Student name: ")
    names.append(name)

    
    age = int(input("Student age: "))        # Get age with validation
    while age < 1 or age > 120:
        print("❌ Invalid age!")
        age = int(input("Student age: "))
    ages.append(age)

    
    mark = int(input("Student mark (0-100): "))         # Get mark with validation
    while mark < 0 or mark > 100:
        print("❌ Invalid mark! Must be 0-100.")
        mark = int(input("Student mark (0-100): "))
    marks.append(mark)

    
    grade = calculate_grade(mark)                             # Calculate and store grade
    grades.append(grade)

    print(f" {name} ({age} years old): {mark} marks - GRADE {grade}")


print("\n" + "=" * 75)
print("ALL STUDENTS")
print("£" * 75)

for i in range(student_count):
    print(f"{i + 1}. {names[i]:15} | Age: {ages[i]:3} | Mark: {marks[i]:3} | Grade: {grades[i]}")

                                

print("\n" + "=" * 75)
print("Stats")
print("=" * 75)


highest_mark = marks[0]                      # Find highest mark
highest_mark_student = 0
for i in range(len(marks)):
    if marks[i] > highest_mark:
        highest_mark = marks[i]
        highest_mark_student = i

print(f" HIGHEST MARK: {names[highest_mark_student]} with {highest_mark} marks (Grade {grades[highest_mark_student]})")


lowest_mark = marks[0]                                # Find lowest mark
lowest_mark_student = 0
for i in range(len(marks)):
    if marks[i] < lowest_mark:
        lowest_mark = marks[i]
        lowest_mark_student = i

print(f" LOWEST MARK: {names[lowest_mark_student]} with {lowest_mark} marks (Grade {grades[lowest_mark_student]})")


youngest_age = ages[0]                        # Find youngest student
youngest_student = 0
for i in range(len(ages)):
    if ages[i] < youngest_age:
        youngest_age = ages[i]
        youngest_student = i

print(f" YOUNGEST STUDENT: {names[youngest_student]} at {youngest_age} years old")


eldest_age = ages[0]                                       # Find eldest student
eldest_student = 0
for i in range(len(ages)):
    if ages[i] > eldest_age:
        eldest_age = ages[i]
        eldest_student = i

print(f" Eldest student: {names[eldest_student]} at {eldest_age} years old")

                                  
total_marks = 0                         # Calculate average mark
for mark in marks:
    total_marks += mark
average_mark = total_marks / student_count
average_grade = calculate_grade(average_mark)

print(f" AVERAGE MARK: {average_mark:.1f} (Grade {average_grade})")

print("=" * 75)

print("Next level is gonna be more detailed :):)")