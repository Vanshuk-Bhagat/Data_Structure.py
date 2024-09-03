# Define a dictionary with car brands as keys and their associated values
car = {"Honda": 10, "Suzuki": 20, "Kia": 30, "Skoda": 40}

# Print the entire dictionary
print(car)  # Output: {'Honda': 10, 'Suzuki': 20, 'Kia': 30, 'Skoda': 40}

# Print the type of the variable 'car'
print(type(car))  # Output: <class 'dict'> - confirms that 'car' is a dictionary

# Add a new key-value pair to the dictionary
car["Tata"] = 50

# Print the updated dictionary to see the added item
print(car)  # Output: {'Honda': 10, 'Suzuki': 20, 'Kia': 30, 'Skoda': 40, 'Tata': 50}

# Update the value associated with the key "Honda"
car["Honda"] = 15

# Print the dictionary again to see the updated value for "Honda"
print(car)  # Output: {'Honda': 15, 'Suzuki': 20, 'Kia': 30, 'Skoda': 40, 'Tata': 50}

# Define another dictionary with bike brands and their values
bike = {"Yamah": 5, "Bajaj": 10}

# Update the 'car' dictionary by adding items from the 'bike' dictionary
car.update(bike)

# Print the final dictionary to see the combined entries from both dictionaries
print(car)  
# Output: {'Honda': 15, 'Suzuki': 20, 'Kia': 30, 'Skoda': 40, 'Tata': 50, 'Yamah': 5, 'Bajaj': 10}
# Remove the key-value pair with the key "Tata" from the dictionary
car.pop("Tata")

# Print the dictionary after removing the "Tata" entry
print(car)  
# Output: {'Honda': 15, 'Suzuki': 20, 'Kia': 30, 'Skoda': 40, 'Yamah': 5, 'Bajaj': 10}
