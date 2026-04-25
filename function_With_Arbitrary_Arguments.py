# Arbitrary Arguments - *args
# If you do not know how many arguments will be passed into your function, add a * before the parameter name.

# This way, the function will receive a tuple of arguments and can access the items accordingly:

# Using *args to accept any number of arguments:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Priyal", "Sakshi", "Nishi")
