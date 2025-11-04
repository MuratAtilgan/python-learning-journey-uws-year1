# Test file for shopping_list.py
# This file tests the core functions without requiring user input

import sys
sys.path.append('/home/user/python-learning-journey-uws-year1/Week9')

# Import the shopping list functions
from shopping_list import (
    shopping_list, view_list, add_to_list,
    find_in_list, delete_from_list
)

print("Testing Shopping List Functions")
print("=" * 75)

# Test 1: Add items to the list
print("\nTest 1: Adding items to the list")
print("-" * 75)
add_to_list("Apples")
add_to_list("Bananas")
add_to_list("Milk")
print(f"Current list: {shopping_list}")
assert len(shopping_list) == 3, "Should have 3 items"
print("✓ Test 1 passed: Items added successfully")

# Test 2: View the list
print("\nTest 2: Viewing the list")
print("-" * 75)
view_list()
print("✓ Test 2 passed: List displayed")

# Test 3: Find an item
print("\nTest 3: Finding an item")
print("-" * 75)
result = find_in_list("Apples")
assert result is True, "Should find Apples"
print("✓ Test 3 passed: Item found")

# Test 4: Find non-existent item
print("\nTest 4: Finding non-existent item")
print("-" * 75)
result = find_in_list("Oranges")
assert result is False, "Should not find Oranges"
print("✓ Test 4 passed: Non-existent item not found")

# Test 5: Delete an item
print("\nTest 5: Deleting an item")
print("-" * 75)
delete_from_list("Bananas")
print(f"Current list: {shopping_list}")
assert len(shopping_list) == 2, "Should have 2 items"
assert "Bananas" not in shopping_list, "Bananas should be removed"
print("✓ Test 5 passed: Item deleted successfully")

# Test 6: Try to add duplicate
print("\nTest 6: Adding duplicate item")
print("-" * 75)
add_to_list("Apples")
assert len(shopping_list) == 2, "Should still have 2 items (no duplicate)"
print("✓ Test 6 passed: Duplicate not added")

# Test 7: Case insensitive operations
print("\nTest 7: Case insensitive operations")
print("-" * 75)
result = find_in_list("MILK")
assert result is True, "Should find MILK (case insensitive)"
print("✓ Test 7 passed: Case insensitive search works")

print("\n" + "=" * 75)
print("ALL TESTS PASSED ✓")
print("=" * 75)
