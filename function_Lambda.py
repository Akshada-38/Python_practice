# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax :
# lambda arguments : expression

# The expression is executed and the result is returned:

# Example 1: Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

# Example 2: Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

# Example 3: Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))