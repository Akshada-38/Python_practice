import json

#The json.dumps() method has parameters to order the keys in the result:
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print("Original JSON:")
print(json.dumps(x, indent=4))
print("\nJSON with sorted keys:")
print(json.dumps(x, indent=4, sort_keys=True))