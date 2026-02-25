# Method 1 : dictionary using curly braces :
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary created using curly braces:", my_dict)

# Method 2 : dictionary using dict() constructor :
my_dict_from_constructor = dict(name="Bob", age=25, city="Los Angeles")
print("Dictionary created using dict() constructor:", my_dict_from_constructor)

# Method 3 : dictionary from list of tuples :
list_of_tuples = [("name", "Charlie"), ("age", 35), ("city", "Chicago")]
my_dict_from_tuples = dict(list_of_tuples)
print("Dictionary created from list of tuples:", my_dict_from_tuples)
