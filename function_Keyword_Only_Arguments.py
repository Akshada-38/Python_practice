#To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, name):
  print("Hello", name)

my_function(name = "Neha")

#Without *,, you are allowed to use positional arguments even if the function expects keyword arguments:


def my_function(name):
  print("Hello", name)

my_function("Priya")

#With *,, you will get an error if you try to use positional arguments:
# def my_function(*, name):
#   print("Hello", name)

# my_function("Emil")
