a=20
b=10

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

# write a program that prints "Pass" if marks are 50 or above, otherwise print "Fail"
marks=30 or 90
if marks>=50:
    print("Pass")
else:
    print("Fail")

# write an if-else statement that checks if the entered password is correct.
# if yes, print "Access Granted", otherwise print "Access Denied".
correct_password = "TechCamp"
password = input("Enter password: ")

if password==correct_password:
    print("Access Granted")
else:
    print("Acces Denied")