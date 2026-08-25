# Method 1 = r"\bain"


import re

txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")



# Method 1 = r"ain\b"


import re

txt = "The rain in Spain"

#Check if "ain" is present at the end of a WORD:

y = re.findall(r"ain\b", txt)

print(y)

if y:
  print("Yes, there is at least one match!")
else:
  print("No match")


