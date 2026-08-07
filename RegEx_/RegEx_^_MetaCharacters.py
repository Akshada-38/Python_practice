import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'  \n  Original String: ", txt)
else:
  print("No match \n  Original String: ", txt)
