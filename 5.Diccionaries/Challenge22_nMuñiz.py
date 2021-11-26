print('Welcome to the Database Admin Program')

log_on_information = {
    'mooman74' : 'alskes145',
    'meramo1986' : 'kehns010101',
    'nickyD' : 'world1star',
    'george2' : 'booo3oha',
    'admin00' : 'admin1234'
}

name = input('\nEnter your username: ')
if name in log_on_information.keys():
    password = input('Enter your password: ')
    if password in log_on_information[name]:
        print(f'\nHello {name}! You are logged in!')
        if name == 'admin00':
            print('\nHere is the current user database')
            for key,val in log_on_information.items():
                print(f'Username: {key}\t Password: {val}')
        else:
            change = input(('Would you like to change your password (y/n)? ')).lower() == 'y'
            if change:
                newP = input('What would you like your new password to be: ')
                if len(newP) < 8:
                    print(f'{newP} not the minimum eight characters.')
                    print(f'\n {name} your password is {password}')
                else:
                    log_on_information[name] = newP
                    print(f'\n {name} your password is {log_on_information[name]}')
            else:
                print('Goodbye!')
    else:
        print('Password incorrect!')
else:
    print('Username not in database, goodbye.')


