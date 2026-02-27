set1 = {
    "name": "John",
    "age": 30,  
    "city": "New York",
    "job": "Developer",
    "hobby": "Photography"

}

# Deleting the entire dictionary using the del keyword

del set1
# Trying to access the deleted dictionary will raise a NameError

try:
    print(set1)

except NameError:
    print("The dictionary 'set1' has been deleted and is no longer accessible.")