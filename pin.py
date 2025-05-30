pin="Password2002"
attempts=3

for i in range(1,attempts+1):
    guess=input('Guess the pin: ')
    guess=str(guess)
    if guess==pin:
        print('You guessed it right')
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            print(f'You have {remaining_attempts} attempts left')
        else:
            print('You have run out of attempts')