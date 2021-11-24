print('Welcome to the Binary/Hexadecimal Converter App')

decimal = int(input('\nCompute binary and hexadecimal values up to the following decimal number: '))
num = []
binar = []
hexa = []

for n in range(1, decimal+1):
    num.append(n)
    binar.append(bin(n))
    hexa.append(hex(n))

print('Generating lists...complete!\n')

print('Using slices, we will now show a portion of each list.')
start = int(input('What decimal number would you like to start at: '))
stop = int(input('What decimal number would you like to stop at: '))

print(f'\nDecimal values from {start} to {stop}:')
for n in range(start-1, stop):
    print(num[n])

print(f'\nBinary values from {start} to {stop}:')
for n in range(start-1, stop):
    print(binar[n])

print(f'\nHexadecimal values from {start} to {stop}:')
for n in range(start-1, stop):
    print(hexa[n])

input(f'\nPress Enter to see all values from 1 to {decimal}')
print('Decimal----Binary----Hexadecimal')
print('-----------------------------------------------------')

for n in range(decimal):
    print(f'{num[n]}----{binar[n]}----{hexa[n]}')