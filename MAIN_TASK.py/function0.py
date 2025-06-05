def triangle_area(height,base):
    area=height*base*0.5
    print(area)

triangle_area(20,10)
triangle_area(30,10)

#create a function that checks if a number is an even or odd number
def check_number(x):
    if x%2==0:
        print("The number is even")
    else:
        print("The number is odd")

check_number(70)
check_number(99)

#create a function to calculate the area of a rectangle
def rectangle_area(length,width):
    area=length*width
    print(area)

rectangle_area(50,40)
rectangle_area(100,70)

#create a function that displays the largest number among 3 numbers
def largest_number(num1,num2,num3):
    if num1>num2 and num1>num3:
        results=num1
    elif num2>num1 and num2>num3:
        results=num2
    else:
        results=num3
    print(f"the largest number is {results}")

largest_number(30,50,20)
largest_number(10,20,30)