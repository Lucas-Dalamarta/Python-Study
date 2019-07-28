#   Challenge 2

# 1) Create a list of names and use a for loop to output the length of each name (len() ).
# 2) Add an if  check inside the loop to only output names longer than 5 characters.
# 3) Add another if  check to see whether a name includes a “n”  or “N”  character.
# 4) Use a while  loop to empty the list of names (via pop() )
def __String():
    return  print('-'*30)


name = ['Luke','Kenobi','Leia','Alderaan','Han Solo']

__String()
print('\nVerifying List\n')
__String()

for i in range(len(name)):
    if len(name[i]) > 5 and ('n' in name[i] or 'N' in name[i]):
        print(name[i],len(name[i]))

__String()
print('\nClearing List\n')
__String()

while len(name) >= 0:
    print(name)
    try:
        name.pop()
    except:
        break

__String()