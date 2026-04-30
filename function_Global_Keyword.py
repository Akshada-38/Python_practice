# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# The global keyword makes the variable global.

#Example 1:
def myfunc():
  global x
  x = 300

myfunc()

print(x)

#Example 2:
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)