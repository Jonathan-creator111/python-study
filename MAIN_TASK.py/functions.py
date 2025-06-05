def triangle_area():
    height=10
    base=5
    area=height*base*0.5
    print(area)

triangle_area()

#create a function that checks if a number is an even or odd number
def check_number():
    x=30
    if x%2==0:
        print("The number is even")
    else:
        print("The number is odd")

check_number()

#create a function to calculate the area of a rectangle
def rectangle_area():
    length=20
    width=15
    area=length*width
    print(area)

rectangle_area()

#create a function that displays the largest number among 3 numbers
def largest_number():
    num1=input("enter first number:")
    num1=int(num1)
    num2=input("enter second number:")
    num2=int(num2)
    num3=input("enter third number:")
    num3=int(num3)

    if num1>num2 and num1>num3:
        print(f"{num1} is the largest number")
    elif num2>num1 and num2>num3:
        print(f"{num2} is the largest number")
    else:
        print(f"{num3} is the largest number")

largest_number()