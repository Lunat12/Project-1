import time

print('Welcome to the prime Number App')
isActive = True

while isActive:
    print('\nEnter 1 to determine if a specific number is prime.')
    print('Enter 2 to determine all prime numbers within a set range.')
    choice = input('Enter your choice 1 or 2: ')

    if choice == '1':
        num = int(input('\nEnter a number to determine if it is prime or not: '))
        prime_status = True
        for i in range(2,num):
            if num % i == 0:
                prime_status = False
                break
        if prime_status:
            print(f'{num} is prime!')
        else:
            print(f'{num} is no prime!')
    elif choice == '2':
        lower = int(input('Enter the lower bound of your range: '))
        upper = int(input('Enter the upper bound of your range: '))
        primes = []

        start_time = time.time()

        for n in range(lower, upper +1):
            if n > 1:
                prime_status = True
                for i in range(2,n):
                    if n % i == 0:
                        prime_status = False
                        break
                if prime_status:
                    primes.append(n)

        end_time = time.time()
        delta_time = round(end_time - start_time,4)

        print(f'\nCalculations took a total of {delta_time} seconds.')
        print(f'The following numbers between {lower} and {upper} are prime:')
        input('Press enter to continue.')
        for n in primes:
            print(n)
    else:
        print('\nUnvalid option')
    
    cont = str(input('Would you like to run the program again (y/n):')).lower() == 'n'
    if cont:
        isActive = False

print('\nThank you for using the program. Have a nice day.')