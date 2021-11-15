import random
num = random.randint(1, 10)
count = 0
guess = int(input('Guess a number between 1 and 10: '))
print('')
count += 1

while guess != num:
    if guess < num:
        print('Your guess was too low.')
    else:
        print('Your guess was too high.')
    guess = int(input('Sorry, guess again: '))
    count += 1
    print('')

print('You guessed it! The correct number was', num, '.')
print('It took you', count, 'guesses.')