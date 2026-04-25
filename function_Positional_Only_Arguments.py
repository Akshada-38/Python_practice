# You can specify that a function can have ONLY positional arguments.

# To specify positional-only arguments, add , / after the arguments:

print("Positional-only arguments:")
def my_function(name, /):
  print("Hello", name)

my_function("Priya")
# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

print("\nWithout the , / you can use keyword arguments:")
def my_function(name):
  print("Hello", name)

my_function(name = "Neha")


### ERROR ###
# With , /, you will get an error if you try to use keyword arguments:
# def my_function(name, /):
#   print("Hello", name)

# my_function(name = "Emil")