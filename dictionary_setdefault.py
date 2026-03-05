data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using the setdefault() method to get the value of key 'b' and set it to 0 if it doesn't exist
value_b = data.setdefault('b', 0)
print("Value of key 'b':", value_b)  # Output: 2

new_value_e = data.setdefault('e', 0)
print("Value of key 'e':", new_value_e)  # Output: 0