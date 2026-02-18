# In set , have multiple methods to remove an item from the set. 
name = {"Riya" , "Suresh" , 100 , "neha" , 12.5 , 500}
roll_no = {1 , 2 , 3 , 4 , 5}


#METHOD 1 :remove an item from the set using remove() method
name.remove("Riya")
print("Updated name set after removing an item using remove() method:", name)

#METHOD 2 :remove an item from the set using discard() method
name.discard("Suresh")
print("Updated name set after discarding an item using discard() method:", name)

#METHOD 3 :remove an item from the set using pop() method
#pop() method removes and returns an arbitrary item from the set. It raises a KeyError if the set is empty.
removed_item = name.pop()
print("Removed item using pop() method:", removed_item)
print("Updated name set after popping an item using pop() method:", name)

#METHOD 4 :remove an item from the set using clear() method
#clear() method removes all items from the set, leaving it empty.
name.clear()
print("Updated name set after clearing all items using clear() method:", name)

#METHOD 5 :remove an item from the set using del keyword
#del keyword can be used to delete the entire set or a specific item from the set.
#To delete the entire set:  
del roll_no
print
