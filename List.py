# Define a list with fruit names
lst = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Print the entire list
print(lst)  # Output: ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

# Print the type of the variable 'lst'
print(type(lst))  # Output: <class 'list'> - confirms that 'lst' is a list

# Access and print the first element of the list (index 0)
print(lst[0])  # Output: Apple

# Access and print the last element of the list (index -1 refers to the last element)
print(lst[-1])  # Output: Elderberry

# Access and print a slice of the list from index 1 to 3 (4 is excluded)
print(lst[1:4])  # Output: ['Banana', 'Cherry', 'Date']

# Print the length of the list (number of elements in the list)
print(len(lst))  # Output: 5

# Define another list with different fruit names
lst1 = ["Fig", "Grape", "Honeydew"]

# Concatenate the two lists and print the result
print(lst + lst1)  
# Output: ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew']

# Repeat the list 'lst' three times and print the result
print(lst * 3)  
# Output: ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

# Concatenate three repetitions of 'lst1' with 'lst' and print the result
print(lst1 * 3 + lst)  
# Output: ['Fig', 'Grape', 'Honeydew', 'Fig', 'Grape', 'Honeydew', 'Fig', 'Grape', 'Honeydew', 'Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
