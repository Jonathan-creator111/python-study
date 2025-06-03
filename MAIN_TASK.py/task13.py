#TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
#Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
#Once you learn functions,revisit this and write this code inside a function.
email="admin@mail.com"
password="Admin@123"
attempts=3

for i in range(1,attempts+1):
    guess=input('Guess the email: ')
    guess=str(guess)
    guess=input('Guess the password: ')
    guess=str(guess)
    if guess==email and password:
        print('Login in Successful')
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            print(f'You have {remaining_attempts} attempts left')
        else:
            print('You have run out of attempts')