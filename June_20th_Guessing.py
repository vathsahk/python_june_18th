import random
print('Namaste, What is your name?')
name=input()
print('Well'+  name  + 'Guess the number which i am thinking between 1 and 20')
secretNumber=random.randint(1,20)
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess=int(input())
    if guess<secretNumber:
        print('Your guess is too low')
    elif guess>secretNumber:
        print('Your guess is too high')
    else:
        break
if guess==secretNumber:
    print('Good job, you guessed it right in' + str(guessesTaken) + 'guesses')
else:
    print('Nope, the number i was thinking' + str(secretNumber))
