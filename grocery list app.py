from datetime import datetime

groceryList = ['Cheese', 'Meat']
#Here we use the imported library to get the current date and time
time = datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

print('Welcome to the Grocery List App.')
print(f'Current Date and Time: {month}/{day} {hour}:{minute}')
print('You currently have Meat and Cheese in your list.')

groceryList.append(str.title(input('\nType of food to add to the grocery list: ')))
groceryList.append(str.title(input('Type of food to add to the grocery list: ')))
groceryList.append(str.title(input('Type of food to add to the grocery list: ')))

print(f'\nHere is your grocery list: \n{groceryList}')
groceryList = sorted(groceryList)
print(f'Here is your grocery list sorted: \n{groceryList}')
print('\nSimulating grocery shopping...')

print(f'\nCurrent grocery list: {len(groceryList)} items \n{groceryList}')
purchased = str.title(input('What food did you just buy: '))
groceryList.remove(purchased)
print(f'Removing {purchased} from list...')

print(f'\nCurrent grocery list: {len(groceryList)} items \n{groceryList}')
purchased = str.title(input('What food did you just buy: '))
groceryList.remove(purchased)
print(f'Removing {purchased} from list...')
'''remove alows us to remove by calling a string pop could have printed what i was 
removing simultaneously but it only reads the spot of the list in integers'''

print(f'\nCurrent grocery list: {len(groceryList)} items \n{groceryList}')
purchased = str.title(input('What food did you just buy: '))
groceryList.remove(purchased)
print(f'Removing {purchased} from list...')

print(f'\nCurrent grocery list: {len(groceryList)} items \n\n{groceryList}')
print(f'\nSorry, the store is out of {groceryList[1]}.')
del groceryList[1]
groceryList.insert(0, str.title(input('What food would you like instead: ')))

print(f'\nHere is what remains on your grocery list: \n{groceryList}')