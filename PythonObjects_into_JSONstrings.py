import json

# Convert Python objects into JSON strings, and print the values:

print("Convert dictionary to JSON string: ")
print(json.dumps({"name": "John", "age": 30}))

print("\nConvert list to JSON string: ")
print(json.dumps(["apple", "bananas"]))

print("\nConvert tuple to JSON string: ")
print(json.dumps(("apple", "bananas")))

print("\nConvert string to JSON string: ")
print(json.dumps("hello"))

print("\nConvert integer to JSON string: ")
print(json.dumps(42))

print("\nConvert float to JSON string: ")
print(json.dumps(31.76))

print("\nConvert boolean to JSON string: ")
print(json.dumps(True))

print("\nConvert null to JSON string: ")
print(json.dumps(None))
