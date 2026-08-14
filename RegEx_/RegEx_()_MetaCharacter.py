#()	Capture and group

import re


txt = "The rain in Spain falls mainly in the plain!"

x = re.findall("(ain)", txt)

print("using '()' MetaCharacter :", x)