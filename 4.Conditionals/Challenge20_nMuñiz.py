import random
print('Welcome to a game of Rock, Paper, Scissors')

many = int(input('\nHow many rounds would you like to play: '))

player = 0
computer = 0

choices = {0 : 'rock', 1 : 'paper', 2 : 'scissors'}

for n in range(1, many+1):
    print(f'\nRound {n}')
    print(f'Player: {player} \t Computer: {computer}')
    pick = str(input('time to pick... rock, paper, scissors : ')).lower()
    
    if pick in choices.values():
        Cpick = random.randint(0,2)
        print(f'\tComputer: {choices[Cpick]}')
        print(f'\tPlayer: {pick}')
        if choices[Cpick] == pick:
            print('\tit is a tie, how boring!')
            print('\tThis round was a tie.')
        else:
            if choices[Cpick] == choices[0] and pick == choices[2] or choices[Cpick] == choices[1] and pick == choices[0] or choices[Cpick] == choices[2] and pick == choices[1]:  
                computer +=1
                if Cpick == 0:
                    print('\trock smashes scissors')
                elif Cpick == 1:
                    print('\tpaper covers rock')
                else:
                    print('\tscissors cut paper')
                print('\tComputer wins this round')

            elif choices[Cpick] == choices[2] and pick == choices[0] or choices[Cpick] == choices[0] and pick == choices[1] or choices[Cpick] == choices[1] and pick == choices[2]: 
                player +=1
                if pick == 'rock':
                    print('\trock smashes scissors')
                elif pick == 'paper':
                    print('\tpaper covers rock')
                else:
                    print('\tscissors cut paper') 
                print('\tYou win this round')
      
    else:
        computer +=1
        print('\tThat is not a valid game option!')
        print('\tComputer gets the point!')
           

print('\nFinal Game Results')
print(f'\tRounds Played: {many}')
print(f'\tPlayer score: {player}')
print(f'\tComputer score: {computer}')

if computer < player:
    print(f'\tWinner: PLAYER!!!')
elif computer > player:
    print(f'\tWinner: Computer :(')
else:
    print(f'\tIt is a tie!')

