thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

keys = list(thisdict.keys())   # Convert keys into list
i = 0

while i < len(keys):
    key = keys[i]
    value = thisdict[key]
    
    print("This is the key:", key)
    print("This is the value:", value)
    
    i += 1