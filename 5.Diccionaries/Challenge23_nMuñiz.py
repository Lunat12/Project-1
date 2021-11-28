print('Welcome to the Yes or No Issue Polling App\n')

issue = input('What is the yes or no issue you will be voting on today: ')
voters = int(input('What is the number of voters you will allow on the issue: '))
password = input('Enter a password for polling results: ')

yes = 0
no = 0
valid = 0
results={}

for n in range(voters):
    name =str(input('\nEnter your full name: ')).title()
    if name in results:
        print('Sorry, it seems that someone with that name has already voted.\n')
    else:
        print(f'Here is our issue: {issue}')
        vote = str(input('What do you think...yes or no: '))[0].lower()
        valid += 1
        if vote == 'y':
            yes += 1
            results[name] = 'yes'
            print(f'Thank you {name}! Your vote of yes has been recorded.')
        elif vote == 'n':
            no += 1
            results[name] = 'no'
            print(f'Thank you {name}! Your vote of yes has been recorded.')
        else:
            results[name] = vote
            print('That is not a yes or no answer, but okay...')
            print(f'Thank you {name} Your vote of {vote}. has been recorded.')

print(f'\nThe following {valid} people voted: ')       
for key in results.keys():
    
    print(f'{key}\n')

print(f'On the following issue: {issue}')
if yes > no:
    print(f'Yes wins! {yes} votes to {no}.')
elif no > yes:
    print(f'No wins! {no} votes to {yes}.')
else:
    print(f'It was a tie! {yes} votes to {no}.')

fullResults = input('\nTo see the voting results enter the admin password: ') == password
if fullResults:
    for key, value in results.items():
        print(f'Voter: {key}\tVote: {value}')
else:
    print('Sorry, that is not the correct password. Goodbye...')
print('\nThank you for using the Yes or No Issue Polling App.')