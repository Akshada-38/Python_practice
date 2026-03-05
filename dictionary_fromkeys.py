data = {
    'a': 1, 
    'b': 2, 
    'c': 3, 
    'd': 4
}

# Using the fromkeys() method to create a new dictionary with the same keys and a default value of 0
new_dict = dict.fromkeys(data.keys(), 0)
print("All data of dictionary with default value 0:", new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0, 'd': 0}