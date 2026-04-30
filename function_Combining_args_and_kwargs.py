# You can use both *args and **kwargs in the same function.

# The order must be:

# regular parameters
# *args
# **kwargs
# Example

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")