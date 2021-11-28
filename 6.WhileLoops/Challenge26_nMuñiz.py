print('Welcome to the Factor Generator App')

isActive = True

while isActive:
    num = int(input('\nEnter a number to determine all factors of that number: '))
    factors = []
    for n in range(1,num+1):
        if num % n == 0:
            factors.append(n)
    print('\nFactors of 44 are:')
    for n in factors:
        print(n)
    print('\nIn summary:')
    for i in range(int(len(factors)/2)):
        print(factors[i], '*', factors[-(i+1)], '=', factors[0] * factors[-(i+1)])
  
    cont = str(input('\nRun again (y/n): ')).lower() == 'n'
    if cont:
        isActive = False

print('\nThank you for using the program. Have a great day.')

