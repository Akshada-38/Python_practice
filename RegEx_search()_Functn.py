import re

txt = "The rain in Spain"
x = re.search(r"\s", txt)

print("Original string:", txt)
print("The first white-space character is located in position:", x.start())

