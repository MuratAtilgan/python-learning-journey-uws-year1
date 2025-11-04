# Week 9 - Shopping List Program
# A complete shopping list manager with add, remove, find, and view functionality

# Global shopping list to store items
shopping_list = []


def menu():
    """Display menu options and get user choice"""
    print()
    print("=" * 75)
    print("SHOPPING LIST MENU")
    print("=" * 75)
    print("1   to ADD an item to the list")
    print("2   to REMOVE an item from the list")
    print("3   to FIND an item in the list")
    print("4   to VIEW the whole list")
    print("5   to QUIT")
    print("=" * 75)

    try:
        option = int(input("Select one of the options >> "))
        return option
    except ValueError:
        return 0  # Return invalid option if non-numeric input


def view_list():
    """Display all items in the shopping list"""
    count = 1
    print()
    print("SHOPPING LIST")
    print("=" * 75)

    if len(shopping_list) == 0:
        print("Your shopping list is currently empty")
    else:
        for item in shopping_list:
            print(f"{count}.\t{item}")
            count += 1

    print("=" * 75)
    print()


def find_in_list(f_item):
    """Search for an item in the shopping list"""
    is_item_in_list = False

    for item in shopping_list:
        if f_item.lower() == item.lower():
            is_item_in_list = True
            position = shopping_list.index(item) + 1
            print(f"'{item}' is number {position} on the list")
            break

    return is_item_in_list


def add_to_list(a_item):
    """Add an item to the shopping list if it doesn't already exist"""
    if find_in_list(a_item) is False:
        shopping_list.append(a_item)
        print(f"'{a_item}' has been added to the list")
    else:
        print(f"'{a_item}' is already in the list")


def delete_from_list(d_item):
    """Remove an item from the shopping list"""
    # Find the item (case-insensitive)
    for item in shopping_list:
        if d_item.lower() == item.lower():
            shopping_list.remove(item)
            print(f"'{item}' has been removed from the list")
            return

    print(f"'{d_item}' is not in the list")


def quit_shopping():
    """Display farewell message and final shopping list"""
    print()
    print("=" * 75)
    print("Thank you for using the Shopping List program")
    print("=" * 75)
    print("Here is your final shopping list:")
    view_list()


def invalid_entry():
    """Display error message for invalid menu selection"""
    print()
    print("INVALID ENTRY - Please select option 1, 2, 3, 4, or 5")
    print()


# Main Program
def main():
    """Main program loop"""
    print("=" * 75)
    print("WELCOME TO THE SHOPPING LIST PROGRAM")
    print("=" * 75)

    while True:
        menu_option = menu()

        if menu_option == 1:
            # ADD an item
            new_item = input("Enter an item to ADD to the list >> ")
            new_item = new_item.strip().title()

            if new_item:
                add_to_list(new_item)
            else:
                print("Item cannot be empty")

            view_list()

        elif menu_option == 2:
            # REMOVE an item
            if len(shopping_list) == 0:
                print("Your shopping list is empty - nothing to remove")
            else:
                view_list()
                remove_item = input("Enter the name of the item to REMOVE >> ")
                remove_item = remove_item.strip().title()

                if remove_item:
                    delete_from_list(remove_item)
                else:
                    print("Item cannot be empty")

            view_list()

        elif menu_option == 3:
            # FIND an item
            find_item = input("What item do you want to FIND? >> ")
            find_item = find_item.strip().title()

            if find_item:
                if find_in_list(find_item) is False:
                    print(f"'{find_item}' is currently not in the list")
                    want_to_add = input(f"Do you want to add '{find_item}' to the list? (1 for Yes, 2 for No) >> ")

                    if want_to_add == "1":
                        add_to_list(find_item)
                        view_list()
                    elif want_to_add == "2":
                        print("Item not added")
                    else:
                        print("Invalid choice")
            else:
                print("Item cannot be empty")

        elif menu_option == 4:
            # VIEW the list
            view_list()

        elif menu_option == 5:
            # QUIT
            quit_shopping()
            break

        else:
            invalid_entry()


# Run the program
if __name__ == "__main__":
    main()
