#Exercise1

number_of_tickets=int(input("How many tickets would you like"))
price_per_ticket=8
total_cost=number_of_tickets*price_per_ticket

print("Total cost of this purchase is=""£",total_cost)

#Exercises 2
number_of_tickets=int(input("How many tickets would you like"))
age=int(input(("How old are you")))

if age <5: 
   ticket_price=0
else:   
   ticket_price=8

total_cost=number_of_tickets*ticket_price

print("Total cost of this purchase is=""£",total_cost)

#Exercises 3
number_of_tickets=int(input("How many tickets would you like"))
age=int(input(("How old are you")))

if age <5: 
   ticket_price=0
elif age < 16:
   ticket_price=2   
else:   
   ticket_price=8

total_cost=number_of_tickets*ticket_price

print("Total cost of this purchase is=""£",total_cost)

#Exercises 4
number_of_tickets=int(input("How many tickets would you like"))
age=int(input(("How old are you")))

if age <5: 
   ticket_price=0
elif age < 16:
   ticket_price=2
elif age > 60:
   ticket_price=5      
else:   
   ticket_price=8

total_cost=number_of_tickets*ticket_price

print("Total cost of this purchase is=""£",total_cost)

#Exercises 5 Mark-Grade

mark=int(input("How many marks did you get of your exam"))

if mark <30:
   grade="E"
elif mark <40:
   grade="D"
elif mark <50:
   grade="C"
elif mark <60:
   grade="B2"
elif mark <70:
   grade="B1"
elif mark <80:
   grade="A3"
elif mark <90:
   grade="A2"
else:
   grade="A1"

if grade < "D" :
   result="PASS"
else:
   result="FAIL"
print("Your examp result is",grade,"and you",result)     

#Lab Question 1

his_name=input("What is your name").strip().lower()

if his_name == "Brian":
   result="He is not the Messiah, he is a very naughty boy"
else:
   result="Name not recognised"

print(result)

#Lab Question 2

number=int(input("What is the number"))

if number <50:
   result="TOO LOW"
elif number >50:
   result="TOO HIGH"
else:
   result="CORRECT"

print(result)

#Lab Question 3

status=input("Are you an UWS student" )
age=int(input("How old are you"))

if status =="Yes":
   membership_fee=0
else:
   if age <18:
      membership_fee=24
   else:
      membership_fee=44

print("Your membership fee is £",membership_fee)

