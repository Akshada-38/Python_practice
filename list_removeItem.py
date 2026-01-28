data = [10 , True , 5.5 , "Hello" , 20 , False , 15.5 , "World" , 30]

#Method 1: Using remove() method
data.remove(True)
print("After removing True using remove():", data)

#Method 2: Using pop() method
data.pop(3)  
print("After removing 'Hello' using pop():", data)

#Method 3: Using clear() method
data.clear()
print("After clearing the list using clear():", data)

#Method 4: Using del statement
data = [10 , True , 5.5 , "Hello" , 20 , False , 15.5 , "World" , 30]
del data
print("After deleting the list No list exists now.")  