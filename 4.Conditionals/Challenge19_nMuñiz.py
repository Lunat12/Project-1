import random

print('Welcome to the Guess My Number App')

name = str(input('\nHello! What is your name: ')).title()
print(f'Well {name}, I am thinking of a number between 1 and 20.')

num = random.randint(1, 20)
counter = 0


for n in range(5):
    guess = int(input('\nTake a guess: '))
    if guess < num:
        print('Your guess is too low.')
        counter +=1
    elif guess > num:
        print('Your guess is too high')
        counter +=1
    else:
        print(f'\nGood job, {name}! You guessed my number in {counter +1} guesses!')
        break

if counter >= 5:
    print(f'Game Over. The number I was thinking of was {num}')


