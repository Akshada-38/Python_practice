# nested while loops for using while loop inside another while loop

i = 1
print("printing i and j values using nested while loops:")
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1