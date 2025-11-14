#Week_3 Exercises 

print("Welcome to TicketTouter PRICE FINDER")

ticket_cost = 8

print("The cost a ticket  for this customer is £",ticket_cost)

#Selection

print("Welcome to TicketTouter PRICE FINDER")

age = int(input("What is the age of the customer?"))

if age < 5:
    ticket_cost=0
else :
    ticket_cost=8

print("The cost a ticket  for this customer is £",ticket_cost)    

#Another Selection Example

print("Welcome to TicketTouter PRICE FINDER")

age = int(input("What is the age of the customer?"))

if age < 5:
    ticket_cost=0
elif age <= 15:
    ticket_cost=2
else:
    ticket_cost=8

print("The cost a ticket  for this customer is £",ticket_cost)   

#Another Selection Example

print("Welcome to TicketTouter PRICE FINDER")

age = int(input("What is the age of the customer?"))

if age < 5:
    ticket_cost=0
elif age <= 15:
    ticket_cost=2
elif age >= 60:
    ticket_cost=5    
else:
    ticket_cost=8

print("The cost a ticket  for this customer is £",ticket_cost)   

#Same example total cost of tickets after making selection 

print("Welcome to TicketTouter PRICE FINDER")

age = int(input("What is the age of the customer?"))

num_of_tickets = int(input("How many tickets would you like"))

total_cost = num_of_tickets*ticket_cost


if age < 5:
    ticket_cost=0
elif age <= 15:
    ticket_cost=2
elif age >= 60:
    ticket_cost=5    
else:
    ticket_cost=8


print("The cost a ticket  for this customer is £",total_cost)  

# Undergraduate student's mark

print("Assessment RESULTS")

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

#Lab3 - Question1

#Could you create a fully commented program that prompts for and reads in a name, then outputs 'He’s not the Messiah, he’s a very naughty boy' if the name equals 'Brian', and outputs 'Name not recognised' otherwise?

#Note:The single equals (=) is used for assignment—it assigns a value to a variable.


his_name =input("What is his name?")


if his_name == "Brian":
    result= "He is not the Messiah, he is a very naughty boy"
else:
    result="Name not recognised" 

print(result)      

#Question 2

#Could you create a fully commented program that prompts for and reads in a whole number, then outputs 'Too low' if it's less than 50, 'Too high' if it's greater than 50, and 'correct' if it's equal to 50?

print("NUMBER BINGO")

number_result=int(input("What is the number"))

if number_result < 50:
    result="Too low"
elif number_result > 50:
    result="Too high"
else:
    result="CORRECT"

print(result)

#Question 3

#Create a fully commented program to : calculate the cost of UWS Gym membership based on the following information: under 18 £24 over 18 £44 UWS student Free
#Free for UWS students; otherwise, £24 if under 18, £44 if over 18

uws_student=input("Are you an UWS student")

age= int(input("What is your age?"))

if uws_student == "Yes":
    cost="0"
else :
    if age < 18 :
        cost= 24
    else :
        cost = 44

print("Your UWS Gym membership cost is £" , cost)                