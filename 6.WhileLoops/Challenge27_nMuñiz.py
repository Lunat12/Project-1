from typing import OrderedDict


print('Welcome to the Even Odd Number Sorter App')
isActive = True

while isActive:
    numbers = input('\Enter in a string of numbers separated by a comma (,): ')

    for c in numbers:
        if c == ' ':
            numbers = numbers.replace(c, '')
    
    num_list = numbers.split(',')

    evens = []
    odds = []

    print('\n---- Result Summary ----')
    for n in num_list:
        n = int(n)
        if n % 2 == 0:
            evens.append(n)
            print(f'\t{n} is even!')
        else:
            odds.append(n)
            print(f'\t{n} is odd!')


    odds = sorted(odds)
    evens = sorted(evens)

    print(f'\nThe following {len(odds)} numbers are odds:')
    for n in odds:
        print('\t',n)
    print(f'\nThe following {len(evens)} numbers are evens:')
    for n in evens:
        print('\t',n)
    
    cont = str(input('\nWould you like to run the program again (y/n): ')).lower() == 'n'
    if cont:
        isActive = False

print('Thank you for using the program. Goodbye.')

