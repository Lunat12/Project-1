print('Welcome to the Multiplication/Exponent Table App')
name = input("\n\nWhat is your name: ")
num = float(input("What number would you like to work with: "))
message = name.title() + ", Math is cool!"
#we use title because we wan't this capitalized
numbers = (1,2,3,4,5,6,7,8,9)
#here we use a tupple because we won't need to change the contents of the list

print(f"\n\n Multiplication Table For {num}\n")
for n in numbers:
  print(f'\t {n} * {num} = {round(n * num,4)}')
  
print(f"\n\n Exponent Table For {num}\n")
for n in numbers:
  print(f'\t {num}**{n} = {round(num**n,4)}')

print('\n',message)
print(f'\t{str.lower(message)}')
print(f'\t\t{str.title(message)}')
print(f'\t\t\t{str.upper(message)}')