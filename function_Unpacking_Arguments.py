# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.

# Unpacking Lists with *
# If you have values stored in a list, you can use * to unpack them into individual arguments:
# Example
# Using * to unpack a list into arguments:

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

# Unpacking Dictionaries with **
# If you have values stored in a dictionary, you can use ** to unpack them into keyword arguments:
# Example

def my_function(name, age):
  return f"Name: {name}, Age: {age}"

person = {"name": "Emil", "age": 25}
result = my_function(**person) # Same as: my_function(name="Emil", age=25)
print(result)
