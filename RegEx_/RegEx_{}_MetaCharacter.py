import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)
y = re.findall("he.{10}", txt)


print("Original string x:", txt)
print("After RegEX of '{}' using x is:", x)
print("After RegEX of '{}' using y is:", y)

