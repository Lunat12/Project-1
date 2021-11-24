print('Welcome to the average Calculator App')

name = input('\nWhat is your name: ')
many = int(input('How many grades would you like to enter: '))

count = 0
grades = []
while count < many:
    grades.append(float(input('enter grade: ')))
    count += 1

grades = sorted(grades)
grades = grades[ : :-1]

print('\nGrades Highest to Lowest')
for n in grades:
    print('\t', n)

print(f'\n{name}s Grade Summary:')
print(f'\tTotal Number of Grades: {many}')
print(f'\tHighest Grade: {grades[0]}')
print(f'\tLowest Grade: {grades[-1]}')

average = 0
for n in grades:
    average = average + n
print(f'\tAverage: {average / many}')

desired = float(input('\nWhat is your desired average: '))
print(f'\nGood luck {name}!')

a = average / many
x = a * many
x = (desired * (many + 1)) - x
x = x/1

print(f'You will need to get a {x} on your next assigment to earn a {desired} average.')

print('\nLets see what your average could have been if you did better/worse on an assigment.')

newList = grades.copy()

change = float(input('What grade would you like to change: '))
newGrade = float(input('What grade would you like to change {change} to: '))

newList.remove(change)
newList.append(newGrade)
newList = sorted(newList)
newList = newList[ : :-1]

print("\n{name}'s New Grade Summary: ")
print(f'\tTotal Number of Grades: {many}')
print(f'\tHighest Grade: {newList[0]}')
print(f'\tLowest Grade: {newList[-1]}')

averageN = 0
for n in newList:
    averageN = averageN + n
print(f'\tAverage: {averageN / many}')

print(f'\nYour new average would be a {averageN/many} compared to your real average of {average/many}!')
print(f'That is a change of {round(averageN/many - average/many,2)} points!')

print('\n Too bad your original grades are still the same!')
print(newList)
print('You should go ask for extra credit!')
