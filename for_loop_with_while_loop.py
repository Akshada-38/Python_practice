# for loop with while loop use in nested way

# for loop
for i in range(1, 6):
    print(f"Outer loop iteration: {i}")
    
    # while loop nested inside for loop
    j = 1
    while j <= 3:
        print(f"  Inner loop iteration: {j}")
        j += 1