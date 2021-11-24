print('Welcome to the Favorite Teachers Program\n')
fav_teachers = []

teacher = input('Who is your first favorite teacher: ').title()
fav_teachers.append(teacher)
teacher = input('Who is your second favorite teacher: ').title()
fav_teachers.append(teacher)
teacher = input('Who is your third favorite teacher: ').title()
fav_teachers.append(teacher)
teacher = input('Who is your fourth favorite teacher: ').title()
fav_teachers.append(teacher)

print(f'\nYour favorite teachers ranked are: {fav_teachers}')
sorterTeachers = sorted(fav_teachers)
print(f'Your favorite teachers alfabethically are: {sorterTeachers}')
print(f'Your favorite teachers in reversed alfabethically order are: {sorterTeachers[ : :-1]}\n')

print(f'\nYour two top teachers are: {fav_teachers[0:2]}')
print(f'Your next two top teachers are: {fav_teachers[2:4]}')
print(f'Your least favorite teacher is: {fav_teachers[-1]}')
print(f'You have a total of {len(fav_teachers)} favorite teachers\n')

fav_teachers.insert(0, input(f'Oops, {fav_teachers[0]} is no longer your first favorite teacher. Who is your new FAVORITE teacher? ')) 

print(f'\nYour favorite teachers ranked are: {fav_teachers}')
sorterTeachers = sorted(fav_teachers)
print(f'Your favorite teachers alfabethically are: {sorterTeachers}')
print(f'Your favorite teachers in reversed alfabethically order are: {sorterTeachers[ : :-1]}\n')

print(f'\nYour two top teachers are: {fav_teachers[0:2]}')
print(f'Your next two top teachers are: {fav_teachers[2:4]}')
print(f'Your least favorite teacher is: {fav_teachers[-1]}')
print(f'You have a total of {len(fav_teachers)} favorite teachers\n')

remTeacher = input(f"You've decided you no longer like a teacher. Which teacher would you like to remove from your list? ")
if remTeacher in fav_teachers:
    fav_teachers.remove(remTeacher)

print(f'\nYour favorite teachers ranked are: {fav_teachers}')
sorterTeachers = sorted(fav_teachers)
print(f'Your favorite teachers alfabethically are: {sorterTeachers}')
print(f'Your favorite teachers in reversed alfabethically order are: {sorterTeachers[ : :-1]}\n')

print(f'\nYour two top teachers are: {fav_teachers[0:2]}')
print(f'Your next two top teachers are: {fav_teachers[2:4]}')
print(f'Your least favorite teacher is: {fav_teachers[-1]}')
print(f'You have a total of {len(fav_teachers)} favorite teachers\n')