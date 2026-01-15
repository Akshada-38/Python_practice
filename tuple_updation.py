tuple_coll = (10 , 20 , 30 , 40 , 50)
print("Original tuple collection is : " , tuple_coll)
tuple_to_list = list(tuple_coll)
tuple_to_list[2] = "New_Value"
list_to_tuple = tuple(tuple_to_list)
print("Updated tuple collection is : " , list_to_tuple)
