marks = int(input("Enter marks: "))

if marks >= 40:
    print("You are Pass")
    
    if marks >= 75:
        print("Distinction")
    else:
        print("No Distinction")
else:
    print("You are Fail")
