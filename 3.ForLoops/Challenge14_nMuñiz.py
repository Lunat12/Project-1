print('Welcome to the Fibonacci Calculator App\n')

num = int(input('How many digits of the Fibonacci sequence would you like to compute: '))

print(f'\nThe first {num} numbers of the Fibonacci sequence are: ')

start = [1,1]
n = 1
print(n)
numList = [1]

for n in range(num-1):
    n = start[1]
    start[1] = start[0] + start[1]
    start[0] = n
    print(n)
    numList.append(n)

print(f'\nThe corresponding Golden Ratio values are: ')

firstN = 1
secondN = 0
for n in range(num-1):
    a = numList[firstN]/ numList[secondN] 
    firstN += 1
    secondN += 1
    print(a)

print(f'\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...')
    