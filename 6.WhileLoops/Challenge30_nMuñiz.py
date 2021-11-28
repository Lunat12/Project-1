from os import WIFCONTINUED
import random
print('--------------------Power-Ball Simulator--------------------')

white_balls = int(input('\nHow many white-balls to draw from for the 5 winning numbers (Normally 69): '))

if white_balls < 5:
    white_balls = 5

red_balls = int(input('How many red-balls to draw from for the 5 winning numbers (Normally 26): '))

if red_balls < 1:
    red_balls = 1

odds = 1
for n in range(5):
    odds = odds * (white_balls - n)
odds = (odds * red_balls)/120

print(f'You have a 1 in {odds} chance of winning this lottery.')
tiket_interval = int(input('Purchase tickets in what interval: '))

winning_numbers  = []

while len(winning_numbers) < 5:
    num = random.randint(1,white_balls)
    if num not in winning_numbers:
        winning_numbers.append(num)
winning_numbers = sorted(winning_numbers)

Pnum = random.randint(1,red_balls)
winning_numbers.append(Pnum)

print('\n\n---------Welcome to the Power-Ball-----------\n')

print("Tonight's winning numbers are:", end=' ')
for n in winning_numbers:
    print(n, end= ' ')
print('\n')
input('Press "Enter" to begin purchasing tikets!!!')

tikets_purchased = 0
isActive = True
tikets_sold = []

while isActive:
    counter = 0
    while counter < tiket_interval:
        lottery_numbers = []
        while len(lottery_numbers) < 5:
            num = random.randint(1,white_balls)
            if num not in lottery_numbers:
                lottery_numbers.append(num)
        lottery_numbers = sorted(lottery_numbers)
        Pnum = random.randint(1,red_balls)
        lottery_numbers.append(Pnum)

        Pnum = random.randint(1,red_balls)
        if lottery_numbers not in tikets_sold:
            tikets_purchased+=1
            tikets_sold.append(lottery_numbers)
            print(lottery_numbers)
            counter += 1

            if winning_numbers == lottery_numbers:
                print('\nWinning ticket numbers:', end=' ')
                for n in winning_numbers:
                    print(n, end= ' ')
                print('\n')
                print(f'Purchased a total of {tikets_purchased} tickets.')
                break
        else:
            print('Losing ticket generated; disregard...')

    
    if tikets_purchased >= tiket_interval:
        print(f'{tikets_purchased} tickets purchased so far with no winners...\n')
    
    isActive = str(input('Keep purchasing tickets (y/n): ')).lower() == 'y'
    if isActive == False:
        print(f'You bought {tikets_purchased} tickets and still lost!')
        print('Better luck next time!')


        


