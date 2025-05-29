x=[10,20,30,40,50]
for i in x:
    print(i)

# create a list of numbers from 1 to 100
# range function used to generate a sequence of numbers
i=list(range(1,101))
print(i)

# iterate through numbers from 1 to 50
# create a list
#loop
numbers=list(range(1,51))
for i in numbers:
    print(i)

# iterate through numbers from 50 to 100
my_number=list(range(50,101))
for i in my_number:
    print(i)

#display even numbers from 1 to 100
even_numbers=list(range(1,101))
for i in even_numbers:
    if i%2==0:
        print(i)

#display odd numbers from 1 to 100
num_ber=list(range(1,101))
for i in num_ber:
    if i%2!=0:
        print(i)

#store even numbers from 20 to 100
even=[]
num=list(range(20,101))
for i in num:
    if i%2==0:
        even.append(i)

print(even)

#store odd numbers from 100 to 150
odd=[]
luck=list(range(100,151))
for i in luck:
    if i%2!=0:
        odd.append(i)

print(odd)

#store the first 10 even numbers from 1 to 100
even=[]
numb=list(range(1,101))
for i in numb:
    if i%2==0:
        even.append(i)
        if len(even)==10:
            break

print(even)

#store the first 10 odd numbers from 1 to 100
odd=[]
turk=list(range(1,101))
for i in turk:
    if i%2!=0:
        odd.append(i)
        if len(odd)==10:
            break

print(odd)