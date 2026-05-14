# The Fibonacci sequence is a classic example where each number is the sum of the two preceding ones. The sequence starts with 0 and 1:
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# The sequence continues indefinitely, with each number being the sum of the two preceding ones.
# We can use recursion to find a specific number in the sequence:
# Example
# Find the 7th number in the Fibonacci sequence:

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))