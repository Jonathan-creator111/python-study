fruits=["Apples","Mangoes",[10,20,["a","b","c"],30],"Oranges","Bananas","Lemons"]
print(fruits)
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[1:4])
print(fruits[2][1])
print(fruits[2][2][1])


my_list=[10,20,30,"Python","HTML"]
my_list[4]="CSS"
print(my_list)
print(len(my_list))


my_list.append("Python")
my_list.append("1000")
my_list.append("Jonathan")
print(my_list)

x=my_list.copy()
my_list.insert(1,99)
print(my_list)
y=[1000,2000,3000]
my_list.extend(y)
print(my_list)
my_list.remove(10)
print(my_list)
my_list.reverse()
print(my_list)


m=[1,30,20,19]
m.sort()
print(m)