import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall(r"\d", txt)
print("original string:", txt)
print("After '\\d' metacharacter:", x)
