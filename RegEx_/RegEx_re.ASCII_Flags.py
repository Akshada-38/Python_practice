import re

txt = "Åland"

# Find all ASCII matches:
print(re.findall(r"\w", txt, re.ASCII))

# Without the flag, \w matches Unicode word characters:
print(re.findall(r"\w", txt))

# Same result using the shorthand re.A flag:
print(re.findall(r"\w", txt, re.A))