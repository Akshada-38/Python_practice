# Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.
# For large datasets, generators save memory:

def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))