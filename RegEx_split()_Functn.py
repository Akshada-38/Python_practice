import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split(r"\s", txt)
print("This is original string: ", txt)
print("\nThis is split string: ", x)
