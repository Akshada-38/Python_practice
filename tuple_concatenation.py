name = ("Neha", "Shivam", "Rohit" , "Satyarth", "Shivansh")
roll_no = (1, 2, 3, 4, 5)

# Adding two tuples using + operator for creating a new tuple
student_info = name + roll_no
print("The student information is (using 3rd tuple) : " , student_info)

# Adding two tuples using += operator for updating the first tuple
name += roll_no
print("The student information is (using += operator for updating first tuple) : " , name)