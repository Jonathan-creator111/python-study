#TASK 12: Using Python or PHP or Java or Ruby or JavaScript
#Write a program that prints the largest of 4 inputs taken as input from a user.
#Once you learn functions,revisit this and write this code inside a function.

num1=input("enter first number: ")
num1=int(num1)
num2=input("enter second number: ")
num2=int(num2)
num3=input("enter third number: ")
num3=int(num3)
num4=input("enter fourth number: ")
num4=int(num4)

if num1>num2 and num1>num3 and num1>num4:
    print(f"{num1} is the largest number")
elif num2>num1 and num2>num3 and num2>num4:
    print(f"{num2} is the largest number")
elif num3>num1 and num3>num2 and num3>num4:
    print(f"{num3} is the largest number")
else:
    print(f"{num4} is the largest number")
