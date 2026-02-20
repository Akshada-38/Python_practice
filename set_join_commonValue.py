set1 = {1, 2, 3, 4, "Rohit", "Sita", "Gita", 5}
set2 = {"Neha", "Rohit", "Sita", 1, 2, 3, 4, "Gita", "Ram"}

#METHOD 1 : intersection() method
common_values = set1.intersection(set2)    
#intersection() method returns a new set containing the common elements between set1 and set2. Since there are no common elements between the two sets, the result will be an empty set.
print("Common values using intersection() method:", common_values)

#METHOD 2 : & operator
common_values = set1 & set2         
#The & operator performs the same operation as the intersection() method, returning a new set with the common elements. Again, since there are no common elements between set1 and set2, the result will be an empty set.
print("Common values using & operator:", common_values)

#METHOD 3 : intintersection_update() method
set1.intersection_update(set2)                          
#The intersection_update() method updates set1 to contain only the common elements between set1 and set2. Since there are no common elements, set1 will be updated to an empty set.
print("Common values using intersection_update() method:", set1)
