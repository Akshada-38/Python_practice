num = (10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100)
print("Original tuple collection is : " , num)
#Unpacking the tuple using asterisk operator
first, *middle, last = num
print("First element:", first)
print("Middle elements:", middle)
print("Last element:", last)