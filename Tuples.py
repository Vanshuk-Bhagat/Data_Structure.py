# Define a tuple with mixed data types
tup = (1, "Tuple", True, "Extraction", False)

# Print the entire tuple
print(tup)  # Output: (1, 'Tuple', True, 'Extraction', False)

# Print the type of the variable 'tup'
print(type(tup))  # Output: <class 'tuple'> - confirms that 'tup' is a tuple

# Access and print the first element of the tuple (index 0)
print(tup[0])  # Output: 1

# Access and print the last element of the tuple (index -1 refers to the last element)
print(tup[-1])  # Output: False

# Access and print a slice of the tuple from index 1 to 3 (4 is excluded)
print(tup[1:4])  # Output: ('Tuple', True, 'Extraction')

# Print the length of the tuple (number of elements in the tuple)
print(len(tup))  # Output: 5

# Define another tuple with different elements
tup1 = ("Hello World", 2, "Tup1")

# Concatenate the two tuples and print the result
print(tup + tup1)  
# Output: (1, 'Tuple', True, 'Extraction', False, 'Hello World', 2, 'Tup1')

# Repeat the tuple 'tup' three times and print the result
print(tup * 3)  
# Output: (1, 'Tuple', True, 'Extraction', False, 1, 'Tuple', True, 'Extraction', False, 1, 'Tuple', True, 'Extraction', False)

# Concatenate three repetitions of 'tup1' with 'tup' and print the result
print(tup1 * 3 + tup)  
# Output: ('Hello World', 2, 'Tup1', 'Hello World', 2, 'Tup1', 'Hello World', 2, 'Tup1', 1, 'Tuple', True, 'Extraction', False)
