set1 = {10 , "Priya" , 20 , 30}
set2 = {100 , 30 , 40 , 50 , 10}

#Method1 : Using symmetric_difference() method for keep all items except duplicates 
set3 = set1.symmetric_difference(set2)
print("Unique elements (from both sets) using symmetric_difference():",set3)

#Method2 : Using ^ operator for keep all items except duplicates
set4 = set1 ^ set2
print("Unique elements (from both sets) using ^ operator:",set4)