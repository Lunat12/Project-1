import random

print('Welcome tot he Coin Toss App')

print('\n I will flip a Coin a set number of times.')
many = int(input('How many times would you like to flip the coin: '))
result = str(input('Would you like to see the result of each flip (y/n): ')[0]).lower() == 'y'

countHeads = 0
countTails = 0

print('\nFlipping\n')

for n in range(many):
    flip = random.randint(0,1)
    if flip == 0:
        countHeads += 1
        if result:
            print('HEADS')
    else:
        countTails += 1
        if result:
            print('TAILS')
    if countTails == countHeads:
        print(f'At {countTails + countHeads}, the number of heads and tails were equal at {countHeads} each.')

print(f'\nResults Of Flipping A Coin {many} Times:')

print('\nSide\tCount\tPercentage')

print(f'Heads\t{countHeads}/{many}\t{round((countHeads/many)*100,2)}%')
print(f'Heads\t{countTails}/{many}\t{round((countTails/many)*100,2)}%')
