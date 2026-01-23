#First Method :
print("1.insert() Method :")
# The insert() method in Python is used to add an item at a specified index in a list.
# Syntax: list.insert(index, item)
#EX :
students = [ "Sakshi", "Rohit", "Anjali", "Vikram" , "Neha"]
print("Before Insertion :", students)
students.insert(2, "Priya")
print("After Insertion  :", students)


print("\n============================== \n")
#Second Method :
print("2.append() Method :")
# The append() method in Python is used to add an item at the end of a list.
# Syntax: list.append(item)
#EX :
rollnos = [101, 102, 103, 104, 105]
print("Before Appending  :", rollnos)
rollnos.append(106)
print("After Appending   :", rollnos)


print("\n============================== \n")
#Third Method :
print("3.extend() Method :")
# The extend() method in Python is used to add all items of an iterable (like a
#Ex :
city = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"]
print("Before Extending  :", city)
new_cities = ["Pune", "Hyderabad", "Ahmedabad"]     
city.extend(new_cities)
print("After Extending   :", city)