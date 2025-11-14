#week 9
#Putting the shopping list together 

def view_list():
    print("VIEW the list")

def add_to_list():
    print("ADD to the list")

def find_in_list():
    print("FIND in the list")

def delete_from_list():
    print("REMOVE from the list")

def quit_shopping():
    print("QUIT ")

def invalid_entry():
    print("INVALID ENTRY- please select option 1,2,3,4,5")

def menu():
    print()
    print("Please select one of the options")
    print("1   to ADD an item to the list")
    print("2   to REMOVE an item from the list")
    print("3   to FIND an item from the list")
    print("4   to VIEW the whole list")
    print("5   to QUIT")
    option=int(input("Select one of the option >>"))
    print()
    return option


#PROGRAM

shopping_list=[]

menu_option=menu()

while True:

    if menu_option == 1:
        add_to_list()
    elif menu_option == 2:
        delete_from_list()
    elif menu_option == 3:
        find_in_list()
    elif menu_option == 4:
        view_list()
    elif menu_option == 5:
        quit_shopping()
        break
    else:
        invalid_entry()

menu_option=menu()

def view_list():
    count=1
    print()
    print("Shopping List")
    print("="*75)
    if len(shopping_list)==0:
        print("Your shopping list currently empty")
    else:
        for item in shopping_list:
            print(f"{count} .\t {item.title()}")

    print()

def find_in_list(f_item):
    is_item_in_list=False
    for item in shopping_list:
        if f_item ==item:
           is_item_in_list=True
           position=shopping_list.index(item)+1
           print(f"{item} is number {position} on the list")
           return is_item_in_list

def add_to_list(a_item):
    if find_in_list(a_item) is False:
        shopping_list.append(a_item)

def delete_from_list(d_item):
    index=shopping_list.index(d_item)
    del shopping_list[index]

def quit_shopping():
    print("Thank you for using the Shopping List program")
    print("Here is your shopping list")
    view_list()

def invalid_entry():
    print("INVALID ENTRY- please select option 1,2,3,4,5")



while True:
    
    if menu_option==1:
        new_item=input("Enter an item to ADD to the list")
        new_item=new_item.title()
        add_to_list(new_item)
        view_list()
    elif menu_option==2:
        print("Which product do you want to remove?")
        remove_item=input("Enter the name ")
        remove_item=remove_item.title()
        if find_in_list(remove_item) is True:
            delete_from_list(remove_item)
        else:
            print(f"{remove_item} is not currently in the list")
        view_list()
    elif menu_option ==3:
        find_item=input("What do you want to check for ?")
        find_item=find_item.title()
        if find_in_list(find_item) is False:
            print(f"{find_item} is currently not in the list")
            print(f"Do you want to add {find_item} in to the list?")
            want_to_add=input("Press 1 for yes , or no for 2")
            if want_to_add==1:
                add_to_list(find_item)
            view_list()
    elif menu_option==4:
        view_list()

    elif menu_option == 5:
        quit_shopping()
        break
    else:
        invalid_entry()


##Pickling 

import pickle

read_pickle_file=open("shopping_list_file.pck","rb")
shopping_list=pickle.load(read_pickle_file)
read_pickle_file.close()


def view_list():
    count = 1
    print()
    print("Shopping List")
    print("=" * 75)
    if len(shopping_list) == 0:
        print("Your shopping list currently empty")
    else:
        for item in shopping_list:
            print(f"{count} .\t {item.title()}")
            count += 1
    print()


def find_in_list(f_item):
    is_item_in_list = False
    for item in shopping_list:
        if f_item == item:
            is_item_in_list = True
            position = shopping_list.index(item) + 1
            print(f"{item} is number {position} on the list")
    return is_item_in_list


def item_exist(f_item):  # add this function as it was printing out non existing item after deleting it still.
    for item in shopping_list:
        if f_item == item:
            return True
    return False


def add_to_list(a_item):
    if find_in_list(a_item) is False:
        shopping_list.append(a_item)


def delete_from_list(d_item):
    index = shopping_list.index(d_item)
    del shopping_list[index]


def quit_shopping():
    print("Thank you for using the Shopping List program")
    print("Here is your shopping list")
    view_list()


def invalid_entry():
    print("INVALID ENTRY- please select option 1,2,3,4,5")


def menu():
    print()
    print("Please select one of the options")
    print("1   to ADD an item to the list")
    print("2   to REMOVE an item from the list")
    print("3   to FIND an item from the list")
    print("4   to VIEW the whole list")
    print("5   to QUIT")
    option = int(input("Select one of the option >>"))
    print()
    return option



menu_option = menu()

while True:

    if menu_option == 1:
        new_item = input("Enter an item to ADD to the list")
        new_item = new_item.title()
        add_to_list(new_item)
        view_list()
    elif menu_option == 2:

        print("Which product do you want to remove?")
        remove_item = input("Enter the name ")
        remove_item = remove_item.title()

        if  item_exist(remove_item):  # I prefer not to use "True"
            delete_from_list(remove_item)
            print(f"{remove_item} has been deleted!")  # better to add this as print out cleaner .
            print("shopping list Updated:")

        else:
            print(f"{remove_item} is not currently in the list")

        view_list()

    elif menu_option == 3:
        find_item = input("What do you want to check for ?")
        find_item = find_item.title()
        if find_in_list(find_item) is False:
            print(f"{find_item} is currently not in the list")
            print(f"Do you want to add {find_item} in to the list?")
            want_to_add = input("Press 1 for yes , or no for 2")
            if want_to_add == 1:
                add_to_list(find_item)
            view_list()
    elif menu_option == 4:
        view_list()

    elif menu_option == 5:
        quit_shopping()
        break
    else:
        invalid_entry()

    menu_option = menu()

    print("List being saved")

    write_pickle_file=open("shopping_list_file.pck","wb")
    pickle.dump(shopping_list,write_pickle_file)
    write_pickle_file.close()
      
#CAR RENTAL
import pickle

print("="*75)
print("WEE CAR HIRE COMPANY")
print("="*75)

#LOAD EXISTING CARS


try:
    car_file = open("cars.pck","rb")
    cars = pickle.load(car_file)
    car_file.close()
    print(f"Loaded {len(cars)} cars from database")
except:
    cars = []
    print("Starting with empty fleet")

print()



#FUNCTION DEFINITIONS


def view_cars():
                                    #Display all cars in fleet
    print("\n"+"="*75)
    print("CURRENT FLEET")
    print("=" * 75)
    
    if len(cars) ==0:
        print("No cars in fleet!")
    else:
        for i in range(len(cars)):
            print(f"CAR {i + 1}: {cars[i][0]} | {cars[i][1]} | {cars[i][2]} | £{cars[i][3]}/day")
    print()


def car_exists(brand, transmission):
                                                    #Check if car already exists
    for car in cars:
        if car[0].lower() == brand.lower() and car[1].lower() ==transmission.lower():
            return True
    return False


def add_car():
                             #Add new car to the fleet 
    print("\n"+"="*75)
    print("ADD NEW CAR")
    print("="*75)
    
    brand = input("Brand: ").title()
    transmission =input("Transmission (Manual/Automatic): ").title()
    
    if car_exists(brand, transmission):
        print(f"{brand} ({transmission}) already in fleet!")
        return
    
    category = input("Category (Economy/Family/Luxury):").title()
    daily_rate =float(input("Daily rate (£):"))
    
    cars.append([brand, transmission, category, daily_rate])
    print(f"{brand} added to fleet!")


def delete_car():
                                    #Remove car from the fleet
    if len(cars) == 0:
        print("No cars to delete!")
        return
    
    print("\n"+"="*75)
    print("DELETE CAR")
    print("="*75)
    
    view_cars()
    
    car_num =int(input("Which car number to delete? >> "))
    
    if 1 <= car_num <= len(cars):
        deleted = cars[car_num - 1]
        del cars[car_num - 1]
        print(f"{deleted[0]} deleted!")
    else:
        print(f"Invalid nntry! Must be between 1 and {len(cars)}")


def search_car():
                             #Search car by brand
    print("\n"+"="*75)
    print("SEARCH CARS")
    print("="*75)
    
    search_term = input("Enter brand to search:").lower()
    
    found = False
    for i, car in enumerate(cars, 1):
        if search_term in car[0].lower():
            print(f"CAR{i}:{car[0]} | {car[1]} | {car[2]} | £{car[3]}/day")
            found = True
    
    if not found:
        print(f"No cars found matching '{search_term}'")


def quit_program():
   
    print("\n"+"="*75)
    print("THANK YOU!")
    print("="*75)
    print(f"Fleet saved:{len(cars)} cars")
    print("=" * 75)


def invalid_entry():
   
    print("Invalid! Please select 1, 2, 3, 4, or 5")


def menu():
    
    print("\n"+"="*75)
    print("MAIN MENU")
    print("="*75)
    print("1 ..... ADD a car")
    print("2 ..... DELETE a car")
    print("3 ..... SEARCH for a car")
    print("4 ..... VIEW all cars")
    print("5 ..... QUIT and save")
    
    choice = input("Option>>>")
    return choice



    #MAIN PROGRAM


menu_option = menu()

while True:
    
    if menu_option =="1":
        add_car()
    
    elif menu_option =="2":
        delete_car()
    
    elif menu_option =="3":
        search_car()
    
    elif menu_option =="4":
        view_cars()
    
    elif menu_option =="5":
        quit_program()
        break
    else:
        invalid_entry()
    
    menu_option = menu()


#SAVE DATA
print("Saving fleet data...")
car_file = open("cars.pck", "wb")
pickle.dump(cars, car_file)
car_file.close()
print("Fleet saved")
print("Goodbye!") 

#HOLIDAY
import pickle

print("="*75)
print("HOLIDAY PLANNER)
print("="*75)


#LOAD EXISTING HOLIDAYS

try:
    hol_file=open("holidays.pck","rb")
    holidays=pickle.load(hol_file)
    hol_file.close()
    print(f"Loaded {len(holidays)} destination(s)")
except:
    holidays =[]
    print("Starting fresh planner")

print()

#FUNCTION DEFINITIONS

def view_holidays():
                              #all destinations
    print("\n"+"="*75)
    print("YOUR DREAM DESTINATIONS")
    print("="*75)
    
    if len(holidays) == 0:
        print("No destinations planned yet!")
    else:
        total = 0
        for i in range(len(holidays)):
            dest, nights, price, cost = holidays[i]
            print(f"{i + 1}. {dest} - {nights} nights @ £{price}/night = £{cost}")
            total += cost
        print(f"\nTotal vacation budget: £{total}")
    print()


def destination_exists(destination):
                                     #Check if destination already planned
    for holiday in holidays:
        if holiday[0].lower() == destination.lower():
            return True
    return False


def add_holiday():
   
    print("\n"+"="*75)
    print("ADD NEW DESTINATION")
    print("="*75)
    
    destination =input("Destination:").title()
    
    if destination_exists(destination):
        print(f"{destination} already planned!")
        return
    
    nights = int(input("How many nights? "))
    price_per_night =float(input("Price per night (£): "))
    total_cost =nights*price_per_night
    
    holidays.append([destination, nights, price_per_night, total_cost])
    print(f"{destination} added! Total cost: £{total_cost}")


def delete_holiday():
    
    if len(holidays) == 0:
        print("\nNo destinations to delete!")
        return
    
    print("\n"+"="*75)
    print("DELETE DESTINATION")
    print("="*75)
    
    view_holidays()
    
    dest_num =int(input("Which destination to remove? >> "))
    
    if 1 <= dest_num <= len(holidays):
        deleted=holidays[dest_num - 1]
        del holidays[dest_num - 1]
        print(f"{deleted[0]} removed from plans!")
    else:
        print(f"Invalid entry! Must be between 1 and {len(holidays)}")


def search_holiday():
    
    print("\n"+"="*75)
    print("SEARCH DESTINATIONS")
    print("="*75)
    
    search=input("Enter destination to search:").lower()
    
    found=False
    for i,holiday in enumerate(holidays,1):
        if search_term in holiday[0].lower():
            print(f"{holiday[0]} - {holiday[1]} nights @ £{holiday[2]}/night = £{holiday[3]}")
            found =True
    
    if not found:
        print(f"No destinations found matching "{search}"")


def quit_program():
    
    print("\n"+"="*75)
    print("ARRIVEDERCI!")
    print("="*75)
    print(f"Saved {len(holidays)} destination(s)")
    print("="*75)


def invalid_entry():
    
    print("Invalid ENTRY! Please select 1, 2, 3, 4, or 5")


def menu():
    
    print("\n"+"="*75)
    print("MAIN MENU")
    print("="*75)
    print("1  ADD destination")
    print("2  DELETE destination")
    print("3  SEARCH destinations")
    print("4  VIEW all destinations")
    print("5  QUIT and save")
    
    choice = input("Option >>> ")
    return choice



#MAIN PROGRAM


menu_option = menu()

while True:
    
    if menu_option == "1":
        add_holiday()
    
    elif menu_option == "2":
        delete_holiday()
    
    elif menu_option == "3":
        search_holiday()
    
    elif menu_option == "4":
        view_holidays()
    
    elif menu_option == "5":
        quit_program()
        break
    
    else:
        invalid_entry()
    
    menu_option = menu()



#SAVE DATA
print("Saving holiday plans...")
hol_file = open("holidays.pck", "wb")
pickle.dump(holidays, hol_file)
hol_file.close()
print("Plans saved ")
print("Happy Holiday!")
    
#RECIPE
import pickle

print("="*75)
print("DELICIOUS FOOD RECIPE")
print("="*75)

try:
    rec_file = open("recipes.pck", "rb")   #LOAD EXISTING RECIPES if not below
    recipes = pickle.load(rec_file)
    rec_file.close()
    print(f"Loaded {len(recipes)} recipe(s) from cookbook")
except:
    recipes = []
    print("Starting with empty recipe book")

print()


#FUNCTION DEFINITIONS

def view_recipes():
   
    print("\n"+"="*75)
    print("RECIPE BOOK")
    print("="*75)
    
    if len(recipes) == 0:
        print("Recipe book is currently empty!")
    else:
        for i in range(len(recipes)):
            print(f"RECIPE {i + 1}: {recipes[i][0]}")
            print("Ingredients:")
            for ing in recipes[i][1]:
                print(f"{ing[0]} {ing[1]} {ing[2]}")
    print()


def recipe_exists(recipe_name):
    
    for recipe in recipes:
        if recipe[0].lower() == recipe_name.lower():
            return True
    return False


def add_recipe():
    
    print("\n"+"="*75)
    print("ADD NEW RECIPE")
    print("="*75)
    
    rec_name = input("Recipe name:").title()
    
    if recipe_exists(rec_name):
        print(f""{rec_name}"" already in recipe book!")
        return
    
    ingredients =[]
    
    ing_count= int(input("How many ingredients? "))
    
    for i in range(ing_count):
        print(f" Ingredient {i + 1}:")
        quantity =input("Quantity: ")
        unit = input("Unit (cups/tsp/grams/etc): ")
        name = input(" Name: ")
        ingredients.append([quantity, unit, name])
    
    recipes.append([rec_name, ingredients])
    print(f""{rec_name}" added to recipe book!")


def delete_recipe():
    
    if len(recipes) == 0:
        print("No recipes to delete!")
        return
    
    print("\n"+"="*75)
    print("DELETE RECIPE")
    print("="*75)
    
    # Show recipes
    for i in range(len(recipes)):
        print(f"{i + 1}. {recipes[i][0]}")
    
    rec_num = int(input("Which recipe number to delete? >> "))
    
    if 1 <= rec_num <= len(recipes):
        deleted = recipes[rec_num - 1]
        del recipes[rec_num - 1]
        print(f""{deleted[0]}" deleted from recipe book!")
    else:
        print(f"Invalid entry! Must be between 1 and {len(recipes)}")


def search_recipe():
    
    print("\n"+"="*75)
    print("SEARCH RECIPES")
    print("="*75)
    
    search= input("Enter recipe name to search: ").lower()
    
    found=False
    for i in range(len(recipes)):
        if search_term in recipes[i][0].lower():
            print(f"FOUND: {recipes[i][0]}")
            print("Ingredients:")
            for ing in recipes[i][1]:
                print(f"{ing[0]} {ing[1]} {ing[2]}")
            found=True
    
    if not found:
        print(f"No recipes found matching "{search_term}"")


def quit_program():
    
    print("\n"+"="*75)
    print("BON APPETITE")
    print("="*75)
    print(f"You have {len(recipes)} recipe(s) saved")
    print("="*75)


def invalid_entry():
    
    print("Invalid Entry! Please select 1, 2, 3, 4, or 5")


def menu():
    
    print("\n" + "=" * 75)
    print("MAIN MENU")
    print("="*75)
    print("1  ADD a recipe")
    print("2  DELETE a recipe")
    print("3  SEARCH for a recipe")
    print("4  VIEW all recipes")
    print("5  QUIT and save")
    
    choice = input("Option >>> ")
    return choice


#MAIN PROGRAM


menu_option = menu()

while True:
    
    if menu_option == "1":
        add_recipe()
    
    elif menu_option == "2":
        delete_recipe()
    
    elif menu_option == "3":
        search_recipe()
    
    elif menu_option == "4":
        view_recipes()
    
    elif menu_option == "5":
        quit_program()
        break
    
    else:
        invalid_entry()
    
    menu_option = menu()


#SAVE DATA
print("Saving recipes...")
rec_file = open("recipes.pck", "wb")
pickle.dump(recipes, rec_file)
rec_file.close()
print("All recipes saved")
print("Hungry?")




import pickle

print("="*75)
print("BOOK LIBRARY")
print("="*75)

#LOAD EXISTING BOOKS

try:
    book_file = open("library.pck","rb")
    books = pickle.load(book_file)
    book_file.close()
    print(f"Loaded {len(books)} book(s) from library")
except:
    books =[]
    print("Starting with empty library")

print()


#FUNCTION DEFINITIONS


def view_books():
    
    print("\n"+"="*75)
    print("LIBRARY COLLECTION")
    print("="*75)
    
    if len(books) == 0:
        print("Your library is currently empty!")
    else:
        for i in range(len(books)):
            print(f"{i + 1}. {books[i][0]} by {books[i][1]} | {books[i][2]} | {books[i][3]} pages")
    print()


def book_exists(title, author):
   
    for book in books:
        if book[0].lower() == title.lower() and book[1].lower() == author.lower():
            return True
    return False

def add_book():
    
    print("\n"+"="*75)
    print("ADD NEW BOOK")
    print("="*75)
    
    title =input("Book title:").title()
    author =input("Author name:").title()
    
    if book_exists(title, author):
        print(f"'{title}' by {author} already in library!")
        return
    
    genre = input("Genre (Fiction/Non-Fiction/Mystery/etc): ").title()
    pages = int(input("Number of pages:"))
    
    books.append([title, author, genre, pages])
    print(f"'{title}' added to library!")


def delete_book():
    
    if len(books) == 0:
        print("No books to delete!")
        return
    
    print("\n"+"="*75)
    print("DELETE BOOK")
    print("="*75)
    
    view_books()
    
    book_num=int(input("Which book number to delete? >> "))
    
    if 1 <= book_num <= len(books):
        deleted = books[book_num - 1]
        del books[book_num - 1]
        print(f"'{deleted[0]}' deleted from library!")
    else:
        print(f"Invalid entry! Must be between 1 and {len(books)}")


def search_book():
    
    print("\n"+"="*75)
    print("SEARCH LIBRARY")
    print("="*75)
    
    search = input("Enter title or author to search: ").lower()
    
    found = False
    for i in range(len(books)):
        if search in books[i][0].lower() or search in books[i][1].lower():
            print(f"FOUND: {books[i][0]} by {books[i][1]} | {books[i][2]} | {books[i][3]} pages")
            found = True
    
    if not found:
        print(f"No books found '{search}'")


def quit_program():
   
    print("\n"+"="*75)
    print("GOOD BYE")
    print("="*75)
    print(f"You have {len(books)} book(s) saved")
    print("=" * 75)


def invalid_entry():
    
    print("Invalid entry! Please select 1, 2, 3, 4, or 5")


def menu():
    """Display menu and get choice"""
    print("\n"+"="*75)
    print("MAIN MENU")
    print("="*75)
    print("1 ADD a book")
    print("2 DELETE a book")
    print("3 SEARCH for a book")
    print("4 VIEW all books")
    print("5 QUIT and save")
    
    choice = input("Option >>> ")
    return choice


#MAIN PROGRAM

menu_option = menu()

while True:
    
    if menu_option == "1":
        add_book()
    
    elif menu_option == "2":
        delete_book()
    
    elif menu_option == "3":
        search_book()
    
    elif menu_option == "4":
        view_books()
    
    elif menu_option == "5":
        quit_program()
        break
    
    else:
        invalid_entry()
    
    menu_option = menu()


#SAVE DATA
print("Saving library data...")
book_file = open("library.pck", "wb")
pickle.dump(books, book_file)
book_file.close()
print("Library saved")
print("Happy reading!")