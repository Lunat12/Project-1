num_strings=['15','100','55','42']
num_ints=[15,100,55,42]
num_floats=[12.4,13.65,20.8,500.4]
num_lists=[[1,2,3],[4,5,6],[7,8,9]]

list_listNames=['num_strings','num_ints','num_floats','num_lists']
current = 0
'''we use current in orden to be able to have a counter that tell us how many times the for has acted and 
use this integer to instruct the print in wich name of the name list should it print each time.'''
list_all=[num_strings,num_ints,num_floats,num_lists]

print("\t\tSummary Table")
#here we used a for because we basically didn't feel like copy pasting all this trice.
for s in list_all:
  print(f"\nThe variable {list_listNames[current]} is a {type(s)}")
  print(f"It contains the elements: {s}")
  print(f"The elements {s[0]} is a {type(s[0])}")
  current= current + 1

num_strings=sorted(num_strings)
num_ints=sorted(num_ints)
print("\nNow sorting num_strings and num_ints...")
print(f"Sorted num_strings: {num_strings}")
print(f"Sorted num_ints: {num_ints}")
print("\nStrings are sorted alphabetically while integers sorted numerically!")