fruits=['Apple','Banana','oranges','melon']

for i in fruits:
    print(i)
numbers=list(range(1,101))
print(numbers)

#literate or loop through numbers from 20 to 40

nums=list(range(20,41))
for i in range(20,41):
    print(i)





#1Write a program that displays a numbers 1 to 50 inside a list.
i=list(range(1,51))
print(i)
#2From 1 above display the ones divisible by 7 or 5 inside a list.
oddnumbers=[]
odd=list(range(1,51))
for i in odd:
    if i%2!=0:
        oddnumbers.append(i)
print(oddnumbers)
#3Find sum and average of values in the range between 10 to 40.

#4Put in a list the first 10 odd numbers between 10 to 50. 
odd_numbers=[]
numb=list(range(10,51))
for i in numb:
    if i%2!=0:
        odd_numbers.append(i)
        if len(odd_numbers)==10:
            break

print(odd_numbers)
#5write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
number=input('enter number: ')
number=int(number)
pln=list(range(11))
for i in pln:
    mult=i*number
    print(f"{number}*{i}={mult}")
#6write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
even_count=0
even_numbers=list(range(1,51))
for i in even_numbers:
    if i%2==0:
        even_count=even_count+1
print(even_count)
#7ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
#Display the total quantity of the 3 above.
ls1 = [ ("Jay", 20), ("Mo", 30), ("Mya", 32) ]
total=0
for i in ls1:
    i=list(i)
    i[1]=int(i[1])
    total=total+i[1]

print(total)