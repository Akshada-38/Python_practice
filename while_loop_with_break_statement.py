# while loop with break statement for breaking out of the loop when a certain condition is met
i = 1
print("The numbers from 1 to 10 (but '5' is met then stop):")
while i < 10:
  print(i)
  if i == 5:
    break
  i += 1