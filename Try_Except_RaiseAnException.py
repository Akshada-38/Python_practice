x = "hello"

try:
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
except TypeError as e:
    print(e)