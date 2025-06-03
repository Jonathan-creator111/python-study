#TASK 6:Using Python or PHP or Java or Ruby or JavaScript
#Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
#Once you learn functions,revisit this and write this code inside a function.

pin="admin@123"
attempts=4

for i in range(1,attempts+1):
    guess=input('Guess the pin: ')
    guess=str(guess)
    if guess==pin:
        print('access is granted')
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            print(f'You have {remaining_attempts} attempts left')
        else:
            print('account is blocked')