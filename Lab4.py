#Week4 Exercises
#Range()

print(list(range(10, 0, -1)))

print(list(range(15, 3, -3)))

print(list(range(10)))
print(list(range(2,12)))
print(list(range(12,2,-2)))
print(list(range(7,-6,-3)))

#for loop exercises

print("Ok,everyone sing along ......")
for counter in range(11):
    print("Na")

print("Hey Jude")

#for loop-Table exercises

print("Eight times table")

for counter in range(10):
    print("8 multiplied by",counter,"=",8*counter)

print("All done")    

#List

the_pythons = ["Chapman","Cleese","Gilliam","Idle","Jones","Palin"]
empty =[]
some_numbers =[7,42,-21.9]
mixed_list =["Circus",31,[19,"ABC"]]

print(the_pythons)
print(empty)
print(some_numbers)
print(mixed_list)

# list-another exercise

the_pythons = ["Chapman","Cleese","Gilliam","Idle","Jones","Palin"]
empty =[]
some_numbers =[7,42,-21.9]
mixed_list =["Circus",31,[19,"ABC"]]

print(the_pythons[2])
print(some_numbers[0])
print(mixed_list[2][1])

#for loops with LISTS

band =["John","Paul","George","Ringo"]

for member in band:
    print(member)
print("The Beatles")    

#Lab4 
#Question 1

print(list(range(10,0,-1)))

print("Blast Off")

#Question 2   
#last even = 2n   and last odd =2n-1  sum=n**

n=13
last_odd= 2*n-1

odd_numbers= list(range(1,last_odd+1,2))

sum_odd_numbers=n**2
print(odd_numbers)
print(sum_odd_numbers)

#Question 2 second way of summing 

n=13
last_odd= 2*n-1

odd_numbers= list(range(1,last_odd+1,2))

sum_odd_numbers=sum(odd_numbers)

print(odd_numbers)
print(sum_odd_numbers)

#Question 3

n=20
last_odd= 2*n-1

odd_numbers= list(range(1,last_odd+1,2))

sum_odd_numbers=sum(odd_numbers)

print(odd_numbers)
print(sum_odd_numbers)




#Question 4

characters = ["Miss Scarlett", "Professor Plum", "Mrs Peacock", 
              "Reverend Green", "Colonel Mustard", "Dr Orchid"]


for name in characters:
    
    verdict = input(f"Do you find the accused, {name}, Guilty or Not Guilty? ")

 
    print(f"You said: {name} is {verdict}.")



