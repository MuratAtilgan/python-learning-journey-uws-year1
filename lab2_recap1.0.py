#Type Caster
#Integer

print(type(37))
print(type(0))
print(type(-13))

#Float

print(type(3.14))
print(type(-17.9))
print(type(0.007))

#String

print(type("HelloWorld"))
print(type("B00654321"))
print(type("G;\Labs"))

#Boolean

print(type(True))
print(type(False))

#Exercise 1

num1=9
num2=26
num3=68

answer=num1+num2+num3

print("The total is" , answer)

#Exercise 2

num1= int(input("What is the first number"))
num2= int(input("What is the second number"))
num3= int(input("What is the third number"))

answer=num1+num2+num3

print("The total is", answer)

#Exercises 3 

num1=56
num2=784.25
name="Brian"

print("num1 is",type(num1))
print("num2 is", type(num2))
print("name is",type(name))

#Exercise 4

num1=25
num2=10

print("ADDITION: num1+num2 =",num1+num2)
print("SUBTRACTION: num1-num2 =",num1-num2)
print("MULTIPLICATION:num1*num2 =",num1*num2)
print("DIVISION:num1/num2 =", num1/num2)

#Exercise 5

num1=5
num2=3

print(num1,"MODULUS",num2,"=",num1%num2)
print(num1,"FLOOR DIVISION",num2,"=",num1//num2)
print(num1,"EXPONENTAL",num2,"=",num1**num2)

#Exercise 6

num1=20
print(num1)
num1+=5
print(num1)
num1-=8
print(num1)
num1*=2
print(num1)
num1/=34
print(num1)


#Exercise 6

string1="Who lets "
string2="the dog out"
string3="Woof"

song_title=string1+string2
first_line=song_title+   4*string3

print(first_line)


#Lab2 recap

#1

print(type(7))
print(type(7.0))
print(type("7"))
print(type(True))
print(type("False"))
print(type("????"))
print(type(16.000))
print(type(16000))
print(type(1698283100))
print(type(123))

#2

print(2+3)
print("2+3")
print("2"+"3")

#3

print("B01830795")

#4
price_per_tin=int(input("How much is a tin"))
number_of_tin=int(input("How many tins do you buy"))
postage_delivery=128


total_cost=price_per_tin*number_of_tin+postage_delivery

print("You total cost is=",total_cost)

#5

name=input("What is your name")
age=int(input("How old are you"))

print("Hello",name,"You dont look a day over",age-5)

