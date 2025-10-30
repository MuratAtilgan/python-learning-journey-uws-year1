#more functions 

string1="I am a lunberjack, and I am ok"
num1=148
num2=1.623
num3=-23

list1=["a","b","c","d","e","f","g"]

print()

#abs() function

print("Using the abs(num3) function on", num3,"gives",abs(num3))    #make numbers positive 
print("\t")

#divmod() function

print("Using  divmod(num1,5) function on",num1,"gives",divmod(num1,5))    #divmod (x,y)    x=floor(x/y) or x=x//y   y=x%y  
print("\t")                                             

#len() function

print("Using the len(string1) function on",string1,"gives",len(string1))  # len() or length means length of the selected string including all and space we use...
print("\t")         #\t -single \n- double 

#round() function

print("Using the round(num2) function on",num2,"gives you",round(num2)) #rounds  to next integer or 
print("\t")
print("Using the round(num2,1) function on",num2,"gives you",round(num2,1)) # if given second argument then act accordingly in this example want 1 decimal number where the number has three 
print("\t")

#slice() function

#print(f"usind the slice(2) function on {list1} gives {list1[slice(2)]}")
print("Using the slice(2) function on", list1,"gives you",list1[slice(2)])          #start:stop:step   starts at 0 stopped at 2 so 0th and 1st 
print("\t")
#print(f"using the slic(2,7) function on {list1} gives {list1[slice(2,7)]}")
print("Using the slice(2,5) function on",list1,"gives you",list1[slice(2,5)])        # starts at 2 and stops at 5(excluding) steps default so 2nd,3rd and 4th  
print("\t")
#print(f"using the slice(2,7,3) function on {list1} gives : {list1[slice(2,7,3)]}")
print("Using the slice(2,7,3) function on",list1,"gives you",list1[slice(2,7,3)])    # starts at 2 stops 7 steps 3  so 2nd and 5th as it stops 7-8 step is 3 so actual stop is 5  "2-5-8"

#External Libraries 
# import math

import math
print("\t")

example1=math.sqrt(16)
print("The square root of 16 is",example1)  #print(f"The square root of 16 is : {example1}")
print("\t")

steak=math.pi
example2=math.cos(steak)  
print("The cosine of pi radians is",example2)    #print(f"The cosine of pi radians is : {example2}")
print("\t")

example3=math.degrees(steak)
print("pi radians as expressed as degrees is",example3) #print(f"pi radians as expressed as degree is:{example3} ")
print("\t")

example4=math.factorial(4)
print("The factorial of 4 (1*2*3*4) is",example4)   #print(f"Factorial 10 is : {example4}")

#more example about libraries

print("Fun things to do with STRINGS")
print("^"*50)
print("\t")
monty_says="and now for something completely different"

print("Capitalize:",monty_says.capitalize())
print("\t")
print("find the index of eth:",monty_says.find("eth"))     #print(f"Find the index of eth : {monty_says.find("eth")}")
print("\t")
print("check if all string in alphabet:",monty_says.isalpha())
print("\t")
print("make string uppercase",monty_says.upper())
print("\t")
print("How many occurances of letter e:",monty_says.count("e"))   #print(f"how many occurans of letter e : {monty_says.count("e")}")

#User defined functions

first_name=input("What is your name?")
print("\t")
surname=input("What is your surname?")
print("\t")

def count_letters(name):
    letters=len(name)
    return letters

fname_count=count_letters(first_name)
sname_count=count_letters(surname)

print("Hi",first_name,surname)
print("\t")
print("You have",fname_count+sname_count,"letters in your name")           #print(f"Your first name and surname has : {fname_count+sname_count} letters")

#another example-cities

city1=input("what is the first city you have visited?")
print("\t")
city2=input("What is the second city you have visited?")
print("\t")
city3=input("What is the third 3 you have visited?")
print("\t")

def count_cities(city):
    characters=len(city)
    return characters

ch_city1=count_cities(city1)
ch_city2=count_cities(city2)
ch_city3=count_cities(city3)

print(f"Cities you have visited in your journey are:{city1},{city2} and {city3}")
print("\t")
print(f"Total letters of visited cities is:{ch_city1+ch_city2+ch_city3}")

#one more example- Favourite players

print("Choose your 5 favourite  football players")
print("\t")
print("="*100)
player_1=input("What is your first player?")
print("\t")
print("="*100)
player_2=input("What is your second player?")
print("\t")
print("="*100)
player_3=input("What is your third player?")
print("\t")
print("="*100)
player_4=input("What is your fourth player?")
print("\t")
print("="*100)
player_5=input("What is your fifth player?")
print("\t")
print("="*100)


def count_players(player):
    players=len(player)
    return players

ply1=count_players(player_1)
ply2=count_players(player_2)
ply3=count_players(player_3)
ply4=count_players(player_4)
ply5=count_players(player_5)

print(f" Your favourite football players are :{player_1} , {player_2},{player_3} , {player_4} and {player_5}")
print("\t")
print("="*100)
print(f"Total number of letters on your selected football players are:{ply1+ply2+ply3+ply4+ply5}")
print("\t")
print("="*100)
print("YOUR FOOTBALL LEGENDS")



#What happens if we want to calculate and output more than one value?

num1=int(input("What is the number one"))
print("\t")
num2=int(input("What is the number two"))
print("\t")
def calculations(n1,n2):
    sum=n1+n2
    subtract=n1-n2
    multiply=n1*n2
    divide=n1/n2
    return [divide,sum,multiply,subtract]  #returns one item - a list of the four answers    

answers=calculations(num1,num2)

print("The function outputs",answers,",","",end="")  # I just want to bring the below line print beside this line . 

print("Which is a ",type(answers))
print("\t")
print("="*70)
print("First element is \t",answers[0])  # \t -- space
print("\t")
print("="*70)
print("Second element is \t",answers[1])
print("\t")
print("="*70)
print("Third element is \t",answers[2])
print("\t")
print("="*70)
print("Fourth element is \t",answers[3])
print("="*70)
print("Thanks for your effort for entering 2 numbers:):)")


#enhanced version

num1=int(input("What is your number ?"))
print("\t")
num2=int(input("what is your number?"))
print("\t")

def calculations(n1,n2):
    Sum=n1+n2
    subtract=n1-n2
    multiply=n1*n2
    divide=n1/n2
    return [divide,Sum,subtract,multiply]

answers=calculations(num1,num2)
total_element=sum(answers)   # total_element=answers[0]+answers[1]+answers[2]+answers[3]

print(f"Functions outputs:{answers}")
print("\t")
print("="*65)
print(f"Which is a {type(answers)} ")
print("\t")
print("="*65)
print(f"First element is{answers[0]}")
print("\t")
print("="*65)
print(f"Second element is {round(answers[1])}")
print("\t")
print("="*65)
print(f"Third element is {floor(answers[2])}")
print("\t")
print("="*65)
print(f"Fourth element is {abs(answers[3])}")
print("\t")
print("="*65)
print(f"The total of element is {total_element}")
print("\t")
print("="*65)
print("CuOpt needed ")

#Lab6 Question1
#Without radians conversion

import math

print(f" I want you to enter 4 different degree between 0-360")
print("\t")
print("="*72)
deg_1=int(input("What is the first degree?"))
print("\t")
print("="*72)
deg_2=int(input("What is the second degree"))
print("\t")
print("="*72)
deg_3=int(input("What is the third degree?"))
print("\t")
print("="*72)
deg_4=int(input("What is the fourth degree?"))
print("\t")
print("="*72)

sinn_1=math.sin(deg_1)
coss_2=math.cos(deg_2)
tann_3=math.tan(deg_3)
cott_4=1/math.tan(deg_3)

print(f"{deg_1} degree is {sinn_1} sine")
print("\t")
print("="*72)
print(f"{deg_2} degree is {coss_2} cosine")
print("\t")
print("="*72)
print(f"{deg_3} degree is {tann_3} tangent")
print("\t")
print("="*72)
print(f"{deg_4} degree is {cott_4} cotangent")
print("\t")
print("="*72)
print("WOWWW")

#now with radians conversion 

import math

print(f" I want you to enter 3 different degree between 0-360")
print("\t")
print("="*72)
deg_1=int(input("What is the first degree?"))
print("\t")
print("="*72)
deg_2=int(input("What is the second degree"))
print("\t")
print("="*72)
deg_3=int(input("What is the third degree?"))
print("\t")
print("="*72)


sinn_1=math.sin(math.radians(deg_1))
coss_2=math.cos(math.radians(deg_2))
tann_3=math.tan(math.radians(deg_3))


print(f"{deg_1} degree is {sinn_1} sine")
print("\t")
print("="*72)
print(f"{deg_2} degree is {coss_2} cosine")
print("\t")
print("="*72)
print(f"{deg_3} degree is {tann_3} tangent")
print("\t")
print("="*72)
print("ALL DONE!!")

#LAb6 Question 2

print("Welcome to Pallindrome word game!! ")
print("\t")
print("*"*78)

name=input("What is the name ?")

if name == name [slice(None,None,-1)]:    #another method if name == name[::-1]:  
    print(f"{name} is PALLINDROME")
else:
    print(f"{name} is not PALLINDROME")

print("\t")
print("="*75)
print("Go back and try another one")


#Lab6 Question 3

while True:
    first_name=input("What is your name ")

    if first_name == "finish":
        print("Session eneded")
        break

    surname=input("What is your surname")

    initial_first_name=first_name[0].upper()  #this will make initial capital

    print("\t")
    print("="*75)
    print(f"Your name is {first_name},{surname}")
    print("\t")
    print("="*75)
    print("All Done")



#another example -Series of Mark to Grade

print("Mark to grade level6")

def calculation_grade(mark):
    if mark < 30:
        gradex="E"
    elif mark < 40:
        gradex="D"
    elif mark < 50:
        gradex="C"
    elif mark < 60:
        gradex="B2"
    elif mark < 70:
        gradex="B1"
    elif mark < 80:
        gradex="A3"
    elif mark <90:
        gradex="A2"
    else:
        gradex="A1"
    return gradex

print("="*75)
print("Level 6")
print("="*75)


student_count =int(input("How many students do you want to assess? "))
print("="*75)


names = []                         #  lists to store student data
ages = []
marks = []
grades = []


for i in range(student_count):                     # Collect data for each student
    print(f"\n STUDENT {i + 1} ")

                                          
    name=input("Student name: ")            # Get name
    names.append(name)                      #taking data from storage

    
    age = int(input("Student age: "))        # Get age with validation
    while age < 1 or age > 120:
        print(" Invalid age!")
        age = int(input("Student age: "))
    ages.append(age)

    
    mark = int(input("Student mark (0-100): "))         # Get mark with validation
    while mark < 0 or mark > 100:
        print(" Invalid mark! Must be 0-100.")
        mark = int(input("Student mark (0-100): "))
    marks.append(mark)

    
    grade = calculation_grade(mark)                             # Calculate and store grade
    grades.append(grade)

    print(f" {name} ({age} years old): {mark} marks - GRADE {grade}")


print("="*75)
print("ALL STUDENTS")
print("£"*75)

for i in range(student_count):
    print(f"{i + 1}. {names[i]} | Age: {ages[i]} | Mark: {marks[i]} | Grade: {grades[i]}")    

                                

print("="*75)
print("Stats")
print("="*75)


highest_mark = marks[0]                      # Find highest mark
highest_mark_student = 0
for i in range(len(marks)):          #len() in range is helping to count elements in correct order #like 0th, 1st, 2nd, 3rd, ..., lastth. 
    if marks[i] > highest_mark:      #We used len() to count characters in "lumberjack" example-string. earlier.
        highest_mark = marks[i]
        highest_mark_student = i

print(f" |HIGHEST MARK: {names[highest_mark_student]}| with |{highest_mark} marks| |Grade {grades[highest_mark_student]}|")


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
average_grade = calculation_grade(average_mark)

print(f" AVERAGE MARK: {average_mark:.1f} (Grade {average_grade})")

print("=" * 75)

print("Next level is gonna be more detailed :):) Next Level7")

