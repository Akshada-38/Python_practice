import re

#Replace all white-space characters with the "*":

txt = "The rain in Spain"
x = re.sub(r"\s", "*", txt)
print("This is the original string:", txt)
print("This is the modified string:", x)
