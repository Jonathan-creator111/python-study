#Task 17: Using Python or PHP or Java or Ruby or JavaScript
#Continue with the same program and calculate an individual’s NHDF using:
# i.e NHDF = gross_salary *  0.015
#Write a normal program but use functions if you feel comfortable.

def calculate_gross_salary(basic_salary,benefits):
    gross_salary=basic_salary+benefits
    return gross_salary

basic_salary=float(input("enter basic salary:"))
benefits=float(input("enter benefits:"))

grossSalary=calculate_gross_salary(basic_salary,benefits)

print(grossSalary)

def individual_NHDF(grossSalary):
    NHDF=grossSalary*0.015
    return NHDF

print(individual_NHDF)