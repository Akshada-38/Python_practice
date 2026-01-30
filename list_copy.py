name = ["Neha" , "Amit" , "Sakshi" , "Aniket" , "Yash"]
name_copy = name.copy()
print("Original list of names is :", name)
print("Copied list of names is :", name_copy)
# changing the copied list to show that original list remains unchanged
name_copy.append("Rohit")
print("After modifying copied list:" , name_copy)
print("Original list remains unchanged :" , name)