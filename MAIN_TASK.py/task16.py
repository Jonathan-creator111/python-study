#TASK 16: Using Python or PHP or Java or Ruby or JavaScript
#Continue with the program above, then use  the gross salary to find the NSSF. 
#To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 
#Write a normal program but use functions if you feel comfortable.

def calculate_gross_salary(basic_salary,benefits):
    gross_salary=basic_salary+benefits
    return gross_salary

basic_salary=float(input("enter basic salary:"))
benefits=float(input("enter benefits:"))

grossSalary=calculate_gross_salary(basic_salary,benefits)

print(grossSalary)

def NSSF_amount(c):
    amount=0.06*grossSalary>1800
    return(amount)

c=float(input("enter amount:"))
c=NSSF_amount(c)
print(c)