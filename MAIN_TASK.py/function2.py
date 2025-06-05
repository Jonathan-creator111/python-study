def triangle_area(height,base):
    area=height*base*0.5
    return(area)

y=int(input("enter height:"))
x=int(input("enter base:"))

xy=triangle_area(x,y)
print(xy)