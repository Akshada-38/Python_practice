# Method 1 = r"\Bain"

import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# Method 2 = r"ain\B"

y = re.findall(r"ain\B", txt)

print(y)

if y:
  print("Yes, there is at least one match!")    
else:
  print("No match")