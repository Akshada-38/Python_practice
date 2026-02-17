name = {"Riya" , "Suresh" , 100 , 500}
#remove an item from the set
name.remove("Riya")
print("Updated name set after removing an item:", name)
#discard an item from the set
name.discard("Suresh")
print("Updated name set after discarding an item:", name)   
#remove an item that is not present in the set (will raise an error)
#name.remove("Amit")
#discard an item that is not present in the set (will not raise an error)
name.discard("Amit")
print("Updated name set after discarding an item that is not present:", name)
