dict1 = {
    "a": 1,
    "b": 2, 
    "c": 3,
    "d": 4,
    "e": 5
}

#METHOD 1 : copy() method
dict2 = dict1.copy()
print("Dict1 :", dict1)
print("Dict2 using copy() Method: ", dict2)
dict2["a"] = 10
print("Dict1 after changing dict2: ", dict1)
print("Dict2 after changing dict2: ", dict2)

print("--------------------------------------------------")

#METHOD 2 : dict() operator
dict3 = dict(dict1)
print("Dict3 using dict() operator: ", dict3)
dict3["b"] = 20
print("Dict1 after changing dict3: ", dict1)
print("Dict3 after changing dict3: ", dict3)

print("===============================================")


#Referance copy
dict4 = dict1
print("Dict4: ", dict4)
dict4["c"] = 30
print("Dict1 after changing dict4: ", dict1)
print("Dict4 after changing dict4: ", dict4)