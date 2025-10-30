# Question 1 

print(type(7))
print(type(7.0))
print(type("7"))
print(type(True))
print(type("false"))
print(type("????"))
print(type(16000))
print(type(16000))  

#Python uses commas to separate items in data structures -16,000 tuples 

# error prefix for octal integers  - 01698283100 
banner_id = "01698283100"
print(type(banner_id))
print(type((1, 2, 3)))

# spaces are not allowed inside number literals in Python tuple

print(type(123))
print(1,2,3)

# Question 2

print(2 + 3)
print("2+3")
print("2"+"3")

# Question 3

phone_number = "07879891783"
print("My phone number is" ,phone_number)
print(type(phone_number))

# Question 4


price_per_tin = 2
postage = 3
num_tins = 5

total_cost = (num_tins * price_per_tin) + postage

print(f"The total cost for {num_tins} tins of Spam is £{total_cost}")

# Question 5

name = input("What is your name? ")
age = int(input("What is your age? "))
younger_age = age - 5

print("Hello " + name + ". You don't look a day over " + str(younger_age))

# Quastion 6

tin_price = int(input("How much is a tin"))

postage = int(input("What is the cost of Postage"))

tin_quantity = int(input("How many tins do you have"))

total_cost = (tin_price*tin_quantity)+postage

print("Total cost is" , "£",total_cost)

#Lab2 Overall

num1 = int(input("What is the first number"))
num2 = int(input("What is the second nunber"))
num3 = int(input("What is the third number"))
answer =num1+num2+num3

print("The total is" , answer)

# Variables and Keywords

num1= 37
num2= 141.66
name = "Brian"

print("num1 is" , type(num1))
print("num2 is ",type(num2))
print("name is " , type(name))

# Arithmetic Operators

num1 = 12
num2 = 3

print("ADDITION num1+num2 =", num1+num2)
print("SUBTRACTION num1-num2 =" , num1-num2)
print("MULTIPLICATION num1*num2 =" ,num1*num2)
print("DIVISION num1/num2 =", num1/num2)

#exercise_modulus_floor_division_exponential

num1 = 7
num2 = 2

print(num1 , "MODULUS" , num2,"=", num1%num2)
print(num1 ,"FLOOR DIVISION" ,num2, "=",num1//num2)
print(num1,"EXPONENTIAL", num2 , "=", num1**num2)

#assignment operators

num1=12
print(num1)
num1+=3
print(num1)
num1-=5
print(num1)
num1*=2
print(num1)
num1 /= 4
print(num1)

#comperasion operators

num1=5
num2=3
print(num1==num2)
print(num1!=num2)
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)

#string oeprators

string1 = "Who let"
string2 = "The Dogs out?"
string3 = "Woof"
song_title = string1 + string2

print(song_title)
first_line= song_title + 4* string3
print(first_line)