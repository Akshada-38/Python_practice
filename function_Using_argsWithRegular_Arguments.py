# Using *args with Regular Arguments
# You can combine regular parameters with *args.

# Regular parameters must come before *args:


def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")