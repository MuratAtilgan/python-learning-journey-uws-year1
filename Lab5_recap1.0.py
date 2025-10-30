# Recap Week5

for i in range(1,5):
    for j in range(1,9):
        print(i*j,"\t",end="")
    print()

print("="*75)

for i in range(1,11):
    for j in range(1,9):
        print(i+j,"\t",end="")
    print()    

for i in range(1,6):
    for j in range(2):
        print(i*j,"\t",end="")
    print()

#iteration use "while" loops 

total=0
number=float(input("Enter a number or 0 to quit  "))
print("="*50)
while (number !=0):
       total =total+number
       number=float(input("Enter a number or 0 to quit"))
print("="*50)
print("Total number is ",total)


#we want program to run at least once regardless the known number entered 

while True:
    number=float(input("Enter the number or 0 to quit"))
    print("="*50)
    print("You have entered",number)
    if number == 0:
       break
print("="*50)
print("Completed")    
print("*"*50)

#while counter

counter=0

while counter <5:
    print("Counter",counter)
    counter +=1
print("//"*50)

counter=0

while counter <10:
    print("Counter",counter)
    counter +=1 

print("£"*75)

#smallest number example

smallest = None
number = float(input("Enter a number (50 to finish): "))

while number != 50:
    if smallest is None or number < smallest:
        smallest = number
    number = float(input("Enter another number (50 to finish): "))
    
if smallest is not None:
    print("The smallest number entered was:", smallest)
else:
    print("No numbers were entered.")


#Enhanced marks to grade 
#ask and list students grade 

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

    student += 1      
    print("Assessment result for this student is GRADE", result)

# we can add student amount ourselves 

print("ASSESSMENT RESULTS")
print("="*50)
student_count=int(input("How many students?"))
student = 0  

while student < student_count:  
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

# average results and average grade and invalid entry check

print("ASSESSMENT RESULTS")
print("="*50)

student_count=int(input("How many students?"))
student = 0  
total_marks=0

while student < student_count:  
    student_result = int(input(f"What is the mark of the student {student+1}? "))

    while student_result < 0 or student_result > 100 :
        print("Invalid entry! mark must be between 0-100")
        student_result = int(input(f"What is the mark of the student {student+1}? "))
    
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
         
    print("="*50)
    student += 1    

    average_mark= total_marks/student_count

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

print("*"*75)
print("Class summary")
print("="*75)
print(f"Total student assessed : {student_count}")
print(f"Average mark : {average_mark} ")
print(f"Average grade : {avg_grade}")

print("$"*75)
print("MISSION ACCOMPLISHED")

#highest and lowest score 

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
    
    while student_result not in range(1,101):           
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


print("=" * 50)
print("CLASS SUMMARY")
print("=" * 50)

print(f"Total students assessed: {student_count}")
print(f"Average mark: {average_mark}")
print(f"Average grade: {avg_grade}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark:{lowest_mark}")

print("=" * 50)

print("getting tired a little")


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