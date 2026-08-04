import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print("original string:", txt)
print("After '[]' metacharacter:", x)
