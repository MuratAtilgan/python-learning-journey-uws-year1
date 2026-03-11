def get_integer(prompt):
                                  ##Keep asking until  enter a valid integer
    while True:
        raw=input(prompt)
        try:
            value=int(raw)
            return value
        except ValueError:
            print("Error: That is not a valid integer. Please try again")


#EXAMPLE 1:ValueError
#Problem:Add two whole numbers entered 
##If enter something that is not a number python raises a ValueError
#Solution:Catch the ValueError and ask to try again

def example_1_value_error():
    print("="*50)
    print("EXAMPLE 1-ValueError")
    print("Adding two whole numbers-safe input")
    print("=" * 50)

    num1 = get_integer("Enter the first number:")
    num2 = get_integer("Enter the second number:")
    result = num1 + num2
    print(f"Result:{num1}+{num2} ={result}")
    print()



##EXAMPLE 2:ZeroDivisionError
##Problem: Divide one number by another.
##If enter 0 as the divisor python raises a ZeroDivisionError
##Solution: Catch the ZeroDivisionError and tell  to try again


def get_non_zero_divisor():                    
                           #Keep asking until  enter a non-zero integer
    while True:
        raw = input("Enter the divisor (cannot be zero): ")
        try:
            value = int(raw)
        except ValueError:
            print("Error: Please enter a whole number")
            continue
        try:
            result=1/value   #will raise ZeroDivisionError if value == 0
            return value
        except ZeroDivisionError:
            print(" Error:Division by zero is not allowed.Please enter a non-zero number")


def example_2_zero_division_error():
    print("="*50)
    print("EXAMPLE 2-ZeroDivisionError")
    print("Dividing two numbers safely")
    print("="*50)

    dividend=get_integer("Enter the number to divide: ")
    divisor=get_non_zero_divisor()
    result=dividend/divisor
    print(f"Result: {dividend}/{divisor}={result:.2f}")
    print()



#EXAMPLE 3:IndexError
#Problem:Access an element in a list by position
#If enter an index that is out of range python raises IndexError
#Solution:Catch IndexError and ask  to try again.


def get_list_item(items):
                                                ##Keep asking until enter a valid list index
    print(f"List contains {len(items)} items (valid positions: 0 to {len(items)-1})")
    while True:
        raw = input("Enter the position number you want to see: ")
        try:
            index=int(raw)
        except ValueError:
            print(" Error: Please enter a whole number")
            continue
        try:
            item=items[index]
            return index, item
        except IndexError:
            print(f" Error: Position {index} does not exist in the list. Try again")


def example_3_index_error():
    print("="*50)
    print("EXAMPLE 3-IndexError")
    print("Accessing a list item by position safely")
    print("="*50)

    fruits=["apple","banana","cherry","date","elderberry"]
    print(f"List:{fruits}")

    index,item =get_list_item(fruits)
    print(f"Item at position {index}:{item}")
    print()



##EXAMPLE 4:TypeError
##Problem:Try to concatenate a string and an integer directly
##Python raises a TypeError because + cannot combine str and int
##Solution: Convert the integer to a string first or catch the TypeError


def example_4_type_error():
    print("="*50)
    print("EXAMPLE 4-TypeError")
    print("Combining a string and a number safely")
    print("="*50)

    name=input("Enter your name:")
    score=get_integer("Enter your score:")

    ##what causes the error 
    try:
        message ="Score for " + name + " is " + score   ##TypeError:str+int
        print(message)
    except TypeError:
        print("  Error caught: Cannot concatenate a string and an integer directly.")
        print("  Fix: Convert the integer to a string using str()")
        message = "Score for " + name + " is " + str(score)
        print(f" Corrected message: {message}")
    print()



###EXAMPLE 5:AttributeError
##Problem:Call a method that does not exist on an object
##Python raises an AttributeError when the attribute/method is not found


def example_5_attribute_error():
    print("="*50)
    print("EXAMPLE 5-AttributeError")
    print("Calling a method that does not exist on an object")
    print("="*50)

    text=input("Enter a word or sentence:")

    try:
        result=text.to_uppercase()   ##AttributeError: str has no to_uppercase()
        print(result)
    except AttributeError:
        print("Error:'to_uppercase()' is not a valid string method.")
        print("Fix: Use the correct method name: upper()")
        result=text.upper()
        print(f" Correct result: {result}")
    print()



##MAIN MENU–Run each example

print("\n"+"="*50)
print(" Week_18_Lab =>> Error Handling Examples")
print("="*50+"\n")

while True:
    print("Choose an example to run:")
    print()
    print("1. ValueError =>>                  invalid integer input")
    print("2. ZeroDivisionError =>>           dividing by zero")
    print("3. IndexError =>>                  out-of-range list access")
    print("4. TypeError =>>                   incompatible types")
    print("5. AttributeError =>>              invalid method call")
    print("6. Run ALL examples in order")
    print("0. Exit")
    print()

    choice=input("\nEnter your choice:").strip()

    if choice=="1":
        example_1_value_error()
    elif choice=="2":
        example_2_zero_division_error()
    elif choice=="3":
        example_3_index_error()
    elif choice=="4":
        example_4_type_error()
    elif choice=="5":
        example_5_attribute_error()
    elif choice=="6":
        example_1_value_error()
        example_2_zero_division_error()
        example_3_index_error()
        example_4_type_error()
        example_5_attribute_error()
    elif choice=="0":
        print("Goodbye!!!")
        break
    else:
        print("Invalid selection.Please enter 1-6 or 0 to exit.\n")

