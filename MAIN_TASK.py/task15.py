#TASK 15: Using Python or PHP or Java or Ruby or JavaScript
#Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
#To find the Kenya NHIF Rate using THIS LINK:  
#Write a normal program but use functions if you feel comfortable.

def calculate_gross_salary(basic_salary,benefits):
    gross_salary=basic_salary+benefits
    return gross_salary

basic_salary=float(input("enter basic salary:"))
benefits=float(input("enter benefits:"))

grossSalary=calculate_gross_salary(basic_salary,benefits)

print(grossSalary)

def calculate_nhif(gross):
    if gross<=5999:
        nhif_contribution=150
    elif gross>=6000 and gross<=7999:
        nhif_contribution=300
    elif gross>=8000 and gross<=11999:
        nhif_contribution=400
    elif gross>=12000 and gross<=14999:
        nhif_contribution=500
    elif gross>=15000 and gross<=19999:
        nhif_contribution=600
    elif gross>=20000 and gross<=24999:
        nhif_contribution=750
    elif gross>=25000 and gross<=29999:
        nhif_contribution=850
    elif gross>=30000 and gross<=34999:
        nhif_contribution=900
    elif gross>=35000 and gross<=39999:
        nhif_contribution=950
    elif gross>=40000 and gross<=44999:
        nhif_contribution=1000
    elif gross>=45000 and gross<=49999:
        nhif_contribution=1100
    elif gross>=50000 and gross<=59999:
        nhif_contribution=1200
    elif gross>=60000 and gross<=69999:
        nhif_contribution=1300
    elif gross>=70000 and gross<=79999:
        nhif_contribution=1400
    elif gross>=80000 and gross<=89999:
        nhif_contribution=1500
    elif gross>=90000 and gross<=99999:
        nhif_contribution=1600

    else:
        nhif_contribution=1700
    return nhif_contribution

NHIF=calculate_nhif(grossSalary)
print(NHIF)