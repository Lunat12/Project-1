import random

thesaurus = {
    "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']
    }

print('Welcome to the Thesaurus App!\n')

print('Choose a word from the thesaurus and I will give you a synonym.\n')
print('Here are the words in the thesaurus: ')
for key in thesaurus.keys():
    print(f'\t-{key}')

sinonim = str(input('\nWhat word would you like a synonym for: ')).lower()
if sinonim in thesaurus:
    print(f'A synonym for {sinonim} is {thesaurus[sinonim][random.randint(0,4)] }')
    more = str(input(f'\nWould you like to see the whole thesaurus (y/n): ')).lower() == 'y'

    if more:
        for key in thesaurus.keys():
            print(f'\n{key} synonyms are: ')
            for val in thesaurus[key]:
                print(f'\t-{val}')
    else:
        print('\nI hope you enjoyed the program. Thank you!')
else:
    print('\nSorry this word is not available.')
