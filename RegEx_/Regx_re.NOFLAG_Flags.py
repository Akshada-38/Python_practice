import re

txt = "Hello World"

x = re.search(r"Hello", txt, re.NOFLAG)

if x:
    print("Match found")
else:
    print("No match")