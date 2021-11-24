import math

print('Welcome to the Factorial Calculator App\n')

num = int(input('what numer would you like to compute the factorial of? '))

print(f'{num}! =', end=' ')
for i in range(num-1):
    print(i + 1, end='*')
print(num)

print('Here is the result from the math library:')
print(f'The factorial of {num} is {math.factorial(num)}\n')

result = 1
for i in range(1, num+1):
    result = result * i
print('Here is the result my own algorithm:')
print(f'The factorial of {num} is {result}\n')

print(f'It is shown twice that {num}! = {result} (whith excitement)')