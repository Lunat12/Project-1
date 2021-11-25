print('Welcome to the Vorter Registration App\n')
name = input('Please enter your name: ')
age = int(input('Please enter your age: '))

parties = ['Republican', 'Democratic', 'Independent', 'Libertarian', 'Green']

if age >= 18:
    print(f'\nCongratulations {name}! You are old enough to register to vote.')
    print('\nHere is a list of the political parties to join.')
    for i in parties:
        print(f'-{i}')
    join = str(input('\nWhat party would you like to join: ')).title()
    if join in parties:
        print(f'Congratilations {name}! You joined the {join} party!\nThat is a major party!')
else:
    print('\nYou are not old enough to vote')
