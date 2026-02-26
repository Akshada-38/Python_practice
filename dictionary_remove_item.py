#Remove item
dict1 = { 
    "name" : "Shreya",
    "rollNo" : 1,
    "sub" : "Python",
    "Marks" : 90,
    "branch" : "AIDS"
}

#Method 1: Using pop() method
dict1.pop("Marks")
print("After removing Marks using pop() method:", dict1)

#Method 2: Using del keyword
del dict1["name"]  # Example of deleting a specific key-value pair
print("After deleting 'name' key using del keyword:", dict1)

#Method 3 : Using popitem() method
dict1.popitem()
print("After removing last item using popitem() method:", dict1)

#Method 4: Using clear() method
dict1.clear()
print("After clearing the dictionary using clear() method :", dict1)

