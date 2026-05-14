# Every recursive function must have two parts:
# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument
# Without a base case, the function would call itself forever, causing a stack overflow error.
# Example
# Identifying base case and recursive case:

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))