#TASK 5: Using Python or PHP or Java or Ruby or JavaScript
#Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
#The goal of this exercise is to think about some internals that programs normally take care of for us. 

num1=input("enter first name: ")
num1=int(num1)
num2=input("enter second name: ")
num2=int(num2)
num3=input("enter third name: ")
num3=int(num3)

if num1>num2 and num1>num3:
    print(f"{num1} is the largest number")
elif num2>num1 and num2>num3:
    print(f"{num2} is the largest number")
else:
    print(f"{num3} is the largest number")
