name = {"Priya" , "Amit" , "Suresh" , "Anjali"}
rollno = {101 , 102 , 103 , 104}
#add list2(rollno) to list1(name)
name.update(rollno)
print("Updated name set:", name)
#only list1(name) is updated and list2(rollno) remains unchanged
print("rollno set remains unchanged:", rollno)