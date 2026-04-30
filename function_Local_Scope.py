# Scope
# A variable is only available from inside the region it is created. This is called scope.

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
# Example
# A variable created inside a function is available inside that function:

def myfunc():
  x = 300
  print(x)

myfunc()

# But it is not available outside the function:
# print(x)  # This would cause an error

#function inside function
#The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()