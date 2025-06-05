#Task 15

# first step is , a function to calculate the gross salary
def calculate_gross_salary(basic_salary,benefits):
    gross_salary=basic_salary+benefits
    return gross_salary

basic_salary=float(input("enter basic salary:"))
benefits=float(input("enter benefits:"))

grossSalary=calculate_gross_salary(basic_salary,benefits)

print(grossSalary)

# function to calculate NHIF

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

    else:
        nhif_contribution=1700
    return nhif_contribution

NHIF=calculate_nhif(grossSalary)
print(NHIF)