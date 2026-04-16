# In functions, we can specify as many arguments as we want, just separate them with a comma.

def my_function(fname, lname):
  print(fname + " " + lname)

#ERROR : This function expects 2 arguments, but gets only 1:
# my_function("Akshay")

my_function("Akshay", "Kumar")
my_function("John", "Doe")
# Note: The number of arguments in the function call should match the number of parameters in the function definition, otherwise you will get an error.