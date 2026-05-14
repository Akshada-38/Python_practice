# Recursion can be used to process lists by handling one element at a time:
# Example
# Calculate the sum of all elements in a list:

def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))