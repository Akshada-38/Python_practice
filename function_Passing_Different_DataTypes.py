#You can send any data type as an argument to a function (string, number, list, dictionary, etc.).

# Sending a list as an argument:

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry", "Mango"]
my_function(my_fruits)