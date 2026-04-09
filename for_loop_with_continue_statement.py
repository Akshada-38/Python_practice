# for loop with continue statement for iterating over a list of numbers and skipping even numbers

fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
print("Fruits in the list (excluding 'banana'):")
for x in fruits:
  if x == "banana":
    continue
  print(x)