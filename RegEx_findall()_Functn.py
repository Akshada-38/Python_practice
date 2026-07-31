import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print("This is text: ", txt)
print("This is the list of occurrences 'ai': ", x)
