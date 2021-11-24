print('welcome to the Basketball Roster Program')
roaster=[]
#here we create an empty list to fill it with the players names, python will already recognize the type of the list.

print(type(roaster))
roaster.insert(0, str.title(input("\nWho is your point guard: ")))
roaster.insert(1, str.title(input("Who is your point shooting guard: ")))
roaster.insert(2, str.title(input("Who is your point small forward: ")))
roaster.insert(3, str.title(input("\nWho is your point power forward: ")))
roaster.insert(4, str.title(input("Who is your point center: ")))

print('\n\tYour starting 5 for the upcoming basketball season')
print(f'\t\tPoint Guard:\t\t{roaster[0]}')
print(f'\t\tShooting Guard:\t\t{roaster[1]}')
print(f'\t\tSmall Forward:\t\t{roaster[2]}')
print(f'\t\tPower Forward:\t\t{roaster[3]}')
print(f'\t\tCenter:\t\t\t{roaster[4]}')

injured_player = roaster[2]
del roaster[2]
print(f'\nOh no, {injured_player} is injured.')
print(f'Your roaster only has {len(roaster)} players.')

added_player = str.title(input(f"Who will take {injured_player}'s spot: "))
roaster.insert(2, added_player)
#we save the names of the injured player and the new player to be able to use them even if they are not on the list.

print('\n\tYour starting 5 for the upcoming basketball season')
print(f'\t\tPoint Guard:\t\t{roaster[0]}')
print(f'\t\tShooting Guard:\t\t{roaster[1]}')
print(f'\t\tSmall Forward:\t\t{roaster[2]}')
print(f'\t\tPower Forward:\t\t{roaster[3]}')
print(f'\t\tCenter:\t\t\t{roaster[4]}')

print(f'\nGood Luck {added_player} you will do great!')
print(f'Your roaster now has {len(roaster)} players.')