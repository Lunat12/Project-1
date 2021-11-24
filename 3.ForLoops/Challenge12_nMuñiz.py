import cmath

print('Welcome to the Quadratic Equation Solver App.\n')
print('A quadratic equation is of the form ax^2 + bx + c = 0')
print('Your solutions can be real or complex numbers.')
print('A complex number has to parts: a + bj')
print('Where a is the real portion and bj is the imaginary portion.')

many = int(input('\nHow many equations would you like to solve today: '))

for n in range(0,many):
    print('\nSolving equation #1\n')
    print('----------------------------------')
    a = float(input('Please enter your value of a (coefficient of x^2): '))
    b = float(input('Please enter your value of b (coefficient of x): '))
    c = float(input('Please enter your value of c (coefficient): '))
    print(f'\nThe solutions to {a}x^2 + {b}x + {c} = 0 are:' )

    print(f'\n\tx1 = ({(-b + cmath.sqrt(b**2-(4*a*c)))/(2*a)})')
    print(f'\tx2 = ({(-b - cmath.sqrt(b**2-(4*a*c)))/(2*a)})')

print('Thank you for using the Quadratic Equation Solver App. Goodbye.')