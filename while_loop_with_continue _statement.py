# while loop with continue statement for skipping a particular iteration
i = 0
print("The numbers from 1 to 10 (but '5' is skipped):")
while i < 10:
  i += 1
  if i == 5:
    continue
  print(i)
  