set1 = {"Neha" , 100 , 45.6 , "Riya" , 20 , 10}
set2 = {"Priya" , 15 , 10 , "Neha" , 23 , 45.6}

#Method 1 : Difference() Method for get the unique elements in set1 using third variable
set3 = set1.difference(set2)
print("Unique item from set1 using difference():", set3)

#Method 2 : difference_update() Method for get the unique elements in set1 without using third variable
set1.difference_update(set2)
print("Unique item from set1 using difference_update():", set1)

#Method 3 : "-" operator for get the unique elements in set1 without using third variable
set1 = {"Neha" , 100 , 45.6 , "Riya" , 20 , 10}
set2 = {"Riya" , 10 , 10 , "Neha" , 23 , 45.6}
set3 = set1 - set2
print("Unique item from set1 using '-' operator:", set3)
