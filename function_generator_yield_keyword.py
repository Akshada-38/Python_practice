# The yield keyword is what makes a function a generator.
# When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off.


def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)