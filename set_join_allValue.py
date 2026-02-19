set1 = {1, 2, 3, 4, 5}
set2 = {"stud1" , "stud2" , "stud3" , "stud4" , "stud5"}

#METHOD 1 : join two sets using union() method
joined_set = set1.union(set2)  #The union() method returns a new set that contains all the unique elements from both sets.
print("Joined set using union() method:", joined_set)

#METHOD 2 : join two sets using update() method
#The update() method adds all the unique elements from one set to another set. It modifies the original set.
set1.update(set2)
print("Joined set using update() method:", set1)

#symbolic operator for union of two sets is | (pipe symbol)
#METHOD 3 : join two sets using | operator
joined_set_symbolic = set1 | set2  #The | operator returns a new set
# that contains all the unique elements from both sets.
print("Joined set using | operator:", joined_set_symbolic)
