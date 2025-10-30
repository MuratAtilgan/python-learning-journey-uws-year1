#Exercises 
#range() function

range(10)

for num in range(10):
        print(num)

print(list(range(10)))

range(12,2,-2)

for banana in range(12,2,-2):
           print(banana)

print(list(range(12,2,-2)))

range(7,-6,-3)

for football in range(7,-6,-3):
            print(football) 

print(list(range(7,-6,-3)))

# for loop 

print("Ok everyone sing along....")

for counter in range(11):
        print("Na")
print("Hey Jude")

# multiplication table

print("12 times table")

for counter in range(1,11):
    print("12 multiplied by",counter,"=",12*counter)  
print("ALL DONE!!")          

#Lists

the_pythons=["Chapman","Cleese","Gilliam","Idle","Jones","Palin"]
empty=[]
some_numbers=[7,42,-21.9]
mixed_list=["Circus",31,[19,"ABC"]]

print(the_pythons)
print(empty)
print(some_numbers)
print(mixed_list)

#access some members start from 0th member

the_pythons=["Chapman","Cleese","Gilliam","Idle","Jones","Palin"]
empty=[]
some_numbers=[7,42,-21.9]
mixed_list=["Circus",31,[19,"ABC"]]

print(the_pythons[2])
print(some_numbers[0])
print(mixed_list[2][1])

# band example

band=["John","Paul","George","Ringo"]

for member in band:
        print(member)
print("THE BEATLES")        

#Use a FOR loop to amend the Marks-to-Grades program to allow you to enter five students’ marks.

print("Assessment RESULTS")

for student in range(5):

        student_result = int(input("What is the mark of the student?"))

        if student_result < 30:
            result="E"
        elif student_result < 40:
            result="D"
        elif student_result < 50:
            result="C"    
        elif student_result < 60:
            result="B2"
        elif student_result < 70:
            result="B1"
        elif student_result < 80:
            result="A3"    
        elif student_result < 90:
            result="A2"    
        else: 
            result="A1"    


print("Assessment result for this student is GRADE",result)  


#Amend the above Marks-to-Grades program to allow you to enter the number of students and then their marks.

print("Assessment RESULTS")

num_of_students=int(input("How many students"))

for student in range(num_of_students):

        student_result = int(input("What is the mark of the student?"))

        if student_result < 30:
            result="E"
        elif student_result < 40:
            result="D"
        elif student_result < 50:
            result="C"    
        elif student_result < 60:
            result="B2"
        elif student_result < 70:
            result="B1"
        elif student_result < 80:
            result="A3"    
        elif student_result < 90:
            result="A2"    
        else: 
            result="A1"    


print("Assessment result for this student is GRADE",result)  

# Amend your two previous versions of the Marks-to-Grades programs to calculate the average mark and grade for the group of students.


print("Assessment RESULTS")

num_of_students = int(input("How many students? "))

total_marks = 0

for student in range(num_of_students):
    student_result = int(input("What is the mark of the student? "))
    total_marks = total_marks + student_result


average_mark = total_marks / num_of_students


if average_mark < 30:
    average_grade = "E"
elif average_mark < 40:
    average_grade = "D"
elif average_mark < 50:
    average_grade = "C"    
elif average_mark < 60:
    average_grade = "B2"
elif average_mark < 70:
    average_grade = "B1"
elif average_mark < 80:
    average_grade = "A3"    
elif average_mark < 90:
    average_grade = "A2"    
else: 
    average_grade = "A1"

print("Average mark:", average_mark, "Average grade:", average_grade)

