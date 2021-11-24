print('Welcome to the Shipping Accounts Program')
users = ['eramom', 'footea', 'davisv', 'papinukt', 'allenj']
name = str(input('\nHello, what is your username: ')).lower()

if name in users:
  print(f'\nHello {name}. Welcome back to your account.')
  print('Current shipping prices are as follows: ')
  print('\nShipping orders 0 to 100: \t $5.10 each')
  print('Shipping orders 100 to 500: \t $5.00 each')
  print('Shipping orders 500 to 1000: \t $4.95 each')
  print('Shipping orders over 1000: \t $4.80 each')

  many = int(input('\nHow many items would you like to ship: '))
  if many < 100:
      print(f'To ship {many} items it will cost you ${many * 5.10 } at $5.10 per item.')
  elif many >= 100 and many < 500:
      print(f'To ship {many} items it will cost you ${many * 5.0 } at $5.0 per item.')
  elif many >= 500 and many < 1000:
      print(f'To ship {many} items it will cost you ${many * 4.95 } at $4.95 per item.')
  else:
      print(f'To ship {many} items it will cost you ${many * 4.80 } at $4.80 per item.')
  
  proceed = input('Would you like to place this order(y/n): ') == 'y'
  if proceed:
      print(f'Okay. Shipping your {many} items')
  else:
      print(f'Okay, no order is being placed at this time')
else:
    print('\nSorry, you do not have an account with us. Goodbye.')

