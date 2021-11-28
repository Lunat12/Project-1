from collections import Counter

print('Welcome to the Frequency Analysis App')
non_letters = ['.',',',':',';','?','¿','¡','!','"', "'",'=','+','(',')','/','&','%',' ','$','€','·','#','@','|','º','ª','{','}',']','[','{','}','_','-','1','2','3','4','5','6','7','8','9','0','\t']
key_phrase_1 = str(input('\nEnter a word or phrase to count the occurrence of each letter: ')).lower()

for c in key_phrase_1:
    if c in non_letters:
        key_phrase_1 = key_phrase_1.replace(c, '')


total_ocurrences = len(key_phrase_1)
key_phrase_1 = sorted(key_phrase_1)
letter_count = Counter(key_phrase_1)

print('\nHere is the frequency analysis from key phrase 1: ')
print(f'\n\tLetter\tOcurrence\tPercentage')
for key, value in letter_count.items():
    percentage = (value / total_ocurrences) * 100
    print(f'\t{key}\t{value}\t{round(percentage,2)}%')

ordered_letter_count = letter_count.most_common()
print('\nLetters ordered from highest occurrence to lowest:')
key_phrase_1_ordered_letters = []
for key in ordered_letter_count:
    key_phrase_1_ordered_letters.append(key[0])
for key in key_phrase_1_ordered_letters:
    print(key, end='')
print('\n')


key_phrase_2 = str(input('\nEnter a word or phrase to count the occurrence of each letter: ')).lower()

for c in key_phrase_2:
    if c in non_letters:
        key_phrase_2 = key_phrase_2.replace(c, '')


total_ocurrences_2 = len(key_phrase_2)
key_phrase_2 = sorted(key_phrase_2)
letter_count_2 = Counter(key_phrase_2)

print('\nHere is the frequency analysis from key phrase 1: ')
print(f'\n\tLetter\tOcurrence\tPercentage')
for key, value in letter_count_2.items():
    percentage_2 = (value / total_ocurrences_2) * 100
    print(f'\t{key}\t{value}\t{round(percentage_2,2)}%')

ordered_letter_count_2 = letter_count_2.most_common()
print('\nLetters ordered from highest occurrence to lowest:')
key_phrase_2_ordered_letters = []
for key in ordered_letter_count_2:
    key_phrase_2_ordered_letters.append(key[0])
for key in key_phrase_2_ordered_letters:
    print(key, end='')
print('\n')