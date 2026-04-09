# For loop with break statement for iterating over a list of numbers and breaking the loop when a specific condition is met.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Numbers in the list(If '5' is found then break):")
for n in numbers:
    if n == 5:
        break
    print(n)