import math 
#we import math in order to be able to do more complex mathematical operations

print("Welcome to the Right Triangle Solver App")
b1 = float(input("\n What is the first leg of the triangle: "))
b2 = float(input("What is the second leg of the triangle: "))

area = round((1/2) * b1 * b2, 3)
hipotenusa = math.sqrt(b2**2 + b1**2)
#You can basically find any formulas you need in google just as in this case :)

print(f'\n For a triangle whit legs of {b1} and {b2} the hypotenuse is {round(hipotenusa, 3)}.')
print(f'For a triangle whit legs of {b1} and {b2} the area is {round(area, 3)}.')