name = {"Neha" , "Rohit" , "Sonia" , "Rahul"}
#unpacking the set elements
a , b , c , d = name
print("The unpacked elements are:")
print(a)
print(b)
print(c)
print(d) 
print("the set(name) is unpacked successfully")   
#unpacking the set elements using a asterisk(*)
a , *b = name
print("The unpacked elements are:") 
print(a)
print(b)
print("the set(name) is unpacked successfully using asterisk(*)")