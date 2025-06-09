#TASK 19: Using Python or PHP or Java or Ruby or JavaScript
#Continue with the same program and find the person's PAYEE using the taxable income above.
#Find the Kenya PAYEE Tax Rate using THIS LINK
#Write a normal program but use functions if you feel comfortable

def PAYEE(monthlybands,tax_rate):
    if monthlybands<24000:
        tax_rate=10
    elif monthlybands>=24001 and monthlybands<=32333:
        tax_rate=25
    elif monthlybands>=32334 and monthlybands<=500000:
        tax_rate=30
    elif monthlybands>=500001 and monthlybands<=800000:
        tax_rate=32.5
    else:
        tax_rate=35

print(PAYEE)