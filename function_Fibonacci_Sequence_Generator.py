# Generators can be used to create the Fibonacci sequence.
# It can continue generating values indefinitely, without running out of memory:

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))