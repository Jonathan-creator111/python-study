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
    num1=30
    num2=50
    num3=20
    if num1>num2 and num1>num3:
        results=num1
    elif num2>num1 and num2>num3:
        results=num2
    else:
        results=num3
    print(f"the largest number is {results}")

largest_number()