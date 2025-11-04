# Week 9 - Shopping List Program

## Overview
A complete shopping list management program that allows users to add, remove, find, and view items in their shopping list.

## Features

### 1. Add Items
- Add items to the shopping list
- Prevents duplicate entries
- Case-insensitive duplicate detection
- Automatic title case formatting

### 2. Remove Items
- Remove items from the shopping list
- Case-insensitive search
- Shows confirmation when item is removed
- Displays warning if item doesn't exist

### 3. Find Items
- Search for items in the list
- Case-insensitive search
- Shows item position if found
- Option to add item if not found

### 4. View List
- Display all items in numbered format
- Shows message if list is empty
- Clean, formatted output

### 5. Quit
- Exit the program gracefully
- Display final shopping list before exiting

## Program Structure

### Functions

- `menu()` - Display menu options and get user choice
- `view_list()` - Display all items in the shopping list
- `find_in_list(f_item)` - Search for an item in the list
- `add_to_list(a_item)` - Add an item to the list
- `delete_from_list(d_item)` - Remove an item from the list
- `quit_shopping()` - Display farewell message and final list
- `invalid_entry()` - Display error message for invalid input
- `main()` - Main program loop

## Key Improvements

1. **Error Handling**: Added try-except for menu input validation
2. **Input Validation**: Checks for empty inputs
3. **Case Insensitivity**: Search and comparison work regardless of case
4. **User Feedback**: Clear messages for all operations
5. **Clean Code Structure**: Well-organized functions with clear purposes
6. **Comments**: Comprehensive documentation throughout

## Usage

Run the program:
```bash
python shopping_list.py
```

## Testing

A test file is included to verify all functions work correctly:
```bash
python test_shopping_list.py
```

## Example Session

```
SHOPPING LIST MENU
1   to ADD an item to the list
2   to REMOVE an item from the list
3   to FIND an item in the list
4   to VIEW the whole list
5   to QUIT
Select one of the options >> 1

Enter an item to ADD to the list >> Apples
'Apples' has been added to the list

SHOPPING LIST
1.	Apples
```

## Learning Outcomes

This program demonstrates:
- Function definitions and calling
- List manipulation (append, remove, search)
- While loops for program flow
- Conditional statements (if/elif/else)
- Input validation
- String methods (lower(), strip(), title())
- Error handling with try-except
- Code organization and structure
