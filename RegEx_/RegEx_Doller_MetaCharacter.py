import re

txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet' \n  Original String: ", txt)
else:
  print("No match \n  Original String: ", txt)
