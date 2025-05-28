#Write a program that:
#Takes a transaction amount and account type ("Standard" or "Premium") as input.
#If the account type is "Standard":
#Check if the amount is above 500:
#If it is, print "Transaction exceeds the limit for Standard accounts."
#If not, print "Transaction approved."
#If the account type is "Premium":
#Check if the amount is above 1,000:
#If it is, print "Transaction exceeds the limit for Premium accounts."
#If not, print "Transaction approved."

accounttype=input("accounttype:")
transactionamount=input("transactionamount:")
transactionamount=int(transactionamount)

if accounttype=="Standard":
    if transactionamount>500:
        print("Transaction exceeds the limit for Standard accounts.")
    else:
        print("Transaction approved")
elif accounttype=="Premium":
    if transactionamount>1000:
        print("Transaction exceeds the limit for Premium accounts.")
    else:
        print("Transaction approved")
else:
    print("Wrong account type")