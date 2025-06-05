def largest_number(num1,num2,num3):
    if num1>num2 and num1>num3:
        results=num1
    elif num2>num1 and num2>num3:
        results=num2
    else:
        results=num3
    print(f"the largest number is {results}")

first=int(input("enter the first number:"))
second=int(input("enter the second number:"))
third=int(input("enter the third number:"))
largest_number(first,second,third)