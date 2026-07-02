#The module named mymodule has one function and one dictionary:

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#Import only the person1 dictionary from the module:

from module_import_from import person1

print (person1["age"])