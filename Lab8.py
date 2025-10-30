# Files-files

str_1 = "John"
str_2 = "Paul"
str_3 = "George"
str_4 = "Ringo"

demo_file = open("demo.txt", "w")

demo_file.write(str_1)
demo_file.write(str_2)
demo_file.write(str_3)
demo_file.write(str_4)
demo_file.write("Fab")
demo_file.write("4")

demo_file.close()

demo_file = open("demo.txt", "r")

content_of_file = demo_file.read()

print(content_of_file)

# pickling

import pickle

str_1 = "Creosote"
nbr_1 = 37
list_1 = [12, "Monkeys"]

demo_pck_file = open("pck_file.pck", "wb")

pickle.dump(str_1, demo_pck_file)
pickle.dump(nbr_1, demo_pck_file)
pickle.dump(list_1, demo_pck_file)
pickle.dump("Quite an assortment", demo_pck_file)

demo_pck_file.close()

demo_pck_file = open("pck_file.pck", "rb")

item1 = pickle.load(demo_pck_file)
item2 = pickle.load(demo_pck_file)
item3 = pickle.load(demo_pck_file)
item4 = pickle.load(demo_pck_file)

print(f"{item1} is a {type(item1)}")
print(f"{item2} is a {type(item2)}")
print(f"{item3} is a {type(item3)}")
print(f"{item4} is a {type(item4)}")

# List revisited- insert,append,delete,find

fruits = ["banana", "apple", "grape"]


def print_fruits():
    print()
    print(f"fruits = {fruits}")
    print()
    print(f"First element of fruits is {fruits[0]}")
    print()
    print(f"last element of fruits is {fruits[-1]}")


print_fruits()

# insert

print("=" * 75)
fruits.insert(1, "orange")
print("after INSERTING")
print_fruits()
print("=" * 75)

# append

fruits.append("raspberry")
print("after APPENDING")
print_fruits()
print("=" * 75)

# delete

del fruits[2]
print("after DELETING")
print_fruits()
print("=" * 75)

# find

print("FINDING")
print(f"The index of grape is {fruits.index("grape")}")

# Pickled files and lists

import pickle

the_list = [["a", 1], ["b", 2], ["c", 3]]

print(the_list)
pickle_demo = open("pickle_demo.pck", "wb")

pickle.dump(the_list, pickle_demo)

pickle_demo.close()


# continue
import pickle

demo_of_pickle = open("pickle_demo.pck", "rb")
my_list = pickle.load(demo_of_pickle)
demo_of_pickle.close()

print("Original Version of the file")
print(my_list)

print("=" * 75)

print("after Appending")
my_list.append(["e", 5])
print(my_list)
print()
print("=" * 75)

print("after Inserting")
my_list.insert(3, ["d", 4])
print(my_list)

demo_of_pickle = open("pickle_demo.pck", "wb")
pickle.dump(my_list, demo_of_pickle)
demo_of_pickle.close()

# Exercise

import pickle  # Program1

list = ["cheese", "flour"]
list_demo = open("list_demo.pck", "wb")  # saves to this file  "wb"
pickle.dump(list, list_demo)
list_demo.close()

import pickle  # Program2

demo_of_list = open("list_demo.pck", "rb")  # read from this file  "rb"
list = pickle.load(demo_of_list)
demo_of_list.close()

list.append("eggs")
list.append("bread")
list.append("milk")
list.append("lettuce")

del list[0]

list.insert(-1, "hazelnut")


print()
print(list)

demo_of_list = open("list_demo.pck", "wb")  # saves back again to this file "wb"
pickle.dump(list, demo_of_list)
demo_of_list.close()

# Lab Question 1-2 together

import pickle

print("=" * 75)
print("SHOPPING LIST")
print("=" * 75)

shopping_list = []

num_ele = int(input("How many elements does your shopping list have"))

for i in range(num_ele):
    print(f"Items{i+1}")
    ele_name = input("Enter your first element")
    Quantity = int(input("How many of this element?"))
    unit = input("Enter unit of element")
    shopping_list.append(f"{Quantity} {unit} {ele_name}")

    file = open("shopping.pck", "wb")
    pickle.dump(shopping_list, file)
    file.close()


# Generate Menu

while True:
    print("=" * 75)
    print("MENU:")
    print("1. Add Element")
    print("2. Delete Element")
    print("3. View List")
    print("4. Quit")
    print("=" * 75)

    choice_x = int(input("Select your menu option").strip())

    if choice_x == 1:
        print("Please add element")
        ele_name = input("Enter your first element")
        Quantity = int(input("How many of this element"))
        shopping_list.append(f"{Quantity} {ele_name}")
        file = open("shopping.pck", "wb")
        pickle.dump(shopping_list, file)
        file.close()

    elif choice_x == 2:
        print("Please delete element")
        del_num = int(input("which number of element do you want to delete"))
        del shopping_list[del_num - 1]
        file = open("shopping.pck", "wb")
        pickle.dump(shopping_list, file)
        file.close()

    elif choice_x == 3:
        print(shopping_list)

    elif choice_x == 4:
        print("Good Bye")
        break
    else:
        print("Invalid Entry")

# we want to built a wee local car hire company

import pickle

print("=" * 75)
print("A WEE CAR HIRE COMPANY")
print("=" * 75)

cars = []

num_of_cars = int(input("How many cars would you like to add"))

for i in range(num_of_cars):
    print(f"Car {i + 1}")
    brand = input("What is the brand of the car?")
    transmission = input("What is transmission of the car? ")
    category = input("what is the category of car-economy,family,luxury?")
    daily_pri = float(input("what is the daily rate of the car"))
    cars.append([brand, transmission, category, daily_pri])

    data_car = open("cars.pck", "wb")
    pickle.dump(cars, data_car)
    data_car.close()

while True:
    print("=" * 75)
    print("MAIN MENU")
    print("=" * 75)
    print("A for adding a new car")
    print("D for removing a car")
    print("V for viewing the list")
    print("Q for exiting the program")

    car_menu_choice = input("Please select an option ").strip()

    if car_menu_choice == "A":

        print("add a new car")
        brand = input("What is the brand of the car?")
        transmission = input("What is transmission of the car? ")
        category = input("what is the category of car-economy,family,luxury?")
        daily_pri = float(input("what is the daily rate of the car"))

        cars.append([brand, transmission, category, daily_pri])
        data_car = open("cars.pck", "wb")
        pickle.dump(cars, data_car)
        data_car.close()

    elif car_menu_choice == "D":

        print("** CAR LIST **")
        for i in range(len(cars)):
            print(
                f"CAR {i + 1}: {cars[i][0]} - {cars[i][1]} - {cars[i][2]} - £{cars[i][3]}/day"
            )

        car_num = int(input("\nWhich CAR number to delete? >> "))
        if car_num < 1 or car_num > len(cars):
            print(f"Invalid entry!! numbers must be between 1 and {len(cars)}")
        else:
            del cars[car_num - 1]
            print(" Car deleted!")

        data_car = open("cars.pck", "wb")
        pickle.dump(cars, data_car)
        data_car.close()

    elif car_menu_choice == "V":
        print("*** WEE CAR FLEET ***")
        for i in range(len(cars)):
            print(
                f"CAR {i + 1}: {cars[i][0]} - {cars[i][1]} - {cars[i][2]} - £{cars[i][3]}/day"
            )

    elif car_menu_choice == "Q":
        print("Good Bye")
        break
    else:
        print("Invalid Entry")


#Holiday Planner

import pickle

print("="*75)
print("HOLIDAY PLANNER")
print("="*75)

holidays=[]

numb_of_dest=int(input("How many destination do you want to add"))

for i in range(numb_of_dest):
    print(f"DESTINATION {i+1}")
    dest=input("What is your destination")
    duration=int(input("how many nights"))
    pri_per_night=int(input("How much is a night?"))
    tot_cost=duration*pri_per_night
    holidays.append([dest,duration,pri_per_night,tot_cost])

    hol_dep=open("holiday.pck","wb")
    pickle.dump(holidays,hol_dep)
    hol_dep.close()


while True:
    print("*"*75)
    print("MENU")
    print("*"*75)
    print("1. Add new Destination")
    print("2. Delete Destination")
    print("3. View list")
    print("4. Exit the program")

    hol_sel=int(input("Enter to navigate"))

    if hol_sel == 1:
        dest = input("What is your destination")
        duration = int(input("how many nights"))
        pri_per_night = int(input("How much is a night?"))
        tot_cost = duration * pri_per_night
        holidays.append([dest, duration, pri_per_night, tot_cost])

        hol_dep = open("holiday.pck", "wb")
        pickle.dump(holidays,hol_dep)
        hol_dep.close()

    elif hol_sel == 2:
        print("HOLIDAY LIST")
        for i in range(len(holidays)):
            print(f"DESTINATION {i + 1}: {holidays[i][0]} {holidays[i][1]} days @ £{holidays[i][2]}/night and total={holidays[i][3]}")

        dest_num=int(input("Which Destination number would you like to delete/remove"))
        if dest_num < 1 or dest_num > len(holidays):
            print(f"Invalid Entry!! Numbers must be between 1 and {len(holidays)}")
        else:
            del holidays[dest_num -1]
            print("Destination deleted")

        hol_dep = open("holiday.pck", "wb")
        pickle.dump(holidays,hol_dep)
        hol_dep.close()


    elif hol_sel == 3:
        for i in range(len(holidays)):
            print(f"DESTINATION {i+1}: {holidays[i][0]} {holidays[i][1]} days @ £{holidays[i][2]}/night and total={holidays[i][3]}")

    elif hol_sel == 4:
        print("Enjoy your Holiday")
        break
    else:
        print("Invalid Entry")

#Getting hungry :):)- Food Recipe 

import pickle

print("="*75)
print("DELICIOUS FOOD RECIPE")
print("="*75)

recipe = []

num_rec = int(input("How many recipes? "))

for r in range(num_rec):
    print(f"RECIPE: {r+1}")
    rec_name = input("What is the name of the Recipe? ")
    
    ingredients = []
    
    ing_rec = int(input("How many ingredients do you add? "))
    
    for i in range(ing_rec):
        print(f"Ingredient {i+1}")
        name = input("Name of ingredient? ")
        quan = int(input("How much/many? "))
        unit = input("Unit of ingredient? ")
        ingredients.append([quan, unit, name])
    
    recipe.append([rec_name, ingredients])
    
    print("\nTODAY'S MENU")
    for i in range(len(recipe)):
        print(f"\n{i+1}. {recipe[i][0]}")
        print("Ingredients:")
        for ing in recipe[i][1]:  
            print(f"   - {ing[0]} {ing[1]} {ing[2]}")
    
    rec_file = open("recipe.pck", "wb")
    pickle.dump(recipe, rec_file)
    rec_file.close()

# MENU
while True:
    print("\n" + "="*75)
    print("MENU")
    print("="*75)
    print("1. ADD NEW RECIPE")
    print("2. REMOVE A RECIPE")
    print("3. VIEW RECIPES")
    print("4. QUIT")
    
    choice_recipe = int(input("Select an option >> "))  
    
    if choice_recipe == 1:
        rec_name = input("What is the name of the Recipe? ")
        
        ingredients = []  
        
        ing_rec = int(input("How many ingredients? "))
        
        for i in range(ing_rec):
            print(f"Ingredient {i+1}")
            name = input("Name of ingredient? ")
            quan = int(input("How much/many? "))
            unit = input("Unit of ingredient? ")
            ingredients.append([quan, unit, name])
        
        recipe.append([rec_name, ingredients])
        
        rec_file = open("recipe.pck", "wb")
        pickle.dump(recipe, rec_file)
        rec_file.close()
        print(" Recipe added!")
    
    elif choice_recipe == 2:
        print("\nTODAY'S MENU")
        for i in range(len(recipe)):
            print(f"{i+1}. {recipe[i][0]}")
        
        del_rec = int(input("\nWhich recipe number to delete? >> "))
        
        if del_rec < 1 or del_rec > len(recipe):  
            print(f"Invalid Entry!! Numbers must be between 1 and {len(recipe)}")
        else:
            del recipe[del_rec - 1]
            print(" Deleted!")
            
            rec_file = open("recipe.pck", "wb")
            pickle.dump(recipe, rec_file)
            rec_file.close()
    
    elif choice_recipe == 3:
        print("\nTODAY'S MENU")
        for i in range(len(recipe)):
            print(f"\n{i+1}. {recipe[i][0]}")
            print("Ingredients:")
            for ing in recipe[i][1]:  
                print(f"   - {ing[0]} {ing[1]} {ing[2]}")  
    
    elif choice_recipe == 4:
        print("GOOD BYE")
        break
    
    else:
        print("INVALID ENTRY")








        
    




    

        



