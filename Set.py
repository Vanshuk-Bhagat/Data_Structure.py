# Define a set with a mix of integers, strings, and boolean values
set1 = {1, "a", 2, "b", True, False}

# Print the type of 'set1' to confirm that it is a set
print(type(set1))  # Output: <class 'set'> - confirms that 'set1' is a set

# Add multiple elements to the set using the 'update()' method
# 'update()' can take any iterable (like a list) and adds each element to the set
set1.update(["Helicopter", "Plane"])

# Print the set after adding new elements
print(set1)  # Output: {False, 1, 2, 'Plane', 'b', 'a', 'Helicopter'}
# Note: The elements in a set are unordered, so the order may differ when printed.

# Remove an element from the set using the 'remove()' method
set1.remove("Plane")

# Print the set after removing the specified element
print(set1)  # Output: {False, 1, 2, 'b', 'a', 'Helicopter'}

# Define another set with some common and some unique elements
set2 = {"a", "b", "c"}

# Define a third set with some common and some unique elements
set3 = {"a", "b", "d", "e"}

# Perform a union of set2 and set3, which combines all elements from both sets
# The 'union()' method returns a new set containing all unique elements from both sets
print(set2.union(set3))  
# Output: {'a', 'b', 'c', 'd', 'e'} - combines elements from both sets

# Perform an intersection of set2 and set3, which returns only the common elements
# The 'intersection()' method returns a new set containing only elements that are in both sets
print(set2.intersection(set3))  
# Output: {'a', 'b'} - only elements common to both sets
