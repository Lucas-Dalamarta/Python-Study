# 1) Create two variables – one with your name and one with your age
global name , age

# 2) Create a function which prints your data as one string
def new_name():
    """Sets variable value given user input.\n
        Return : Str"""
    return input('Enter your name : ')


def new_age():
    """Sets variable value given user input.\n
        Return : Int"""
    return int(input('Enter your age : '))


# 3) Create a function which prints ANY data (two arguments) as one string
def return_all(name,age):   
    """Prints Name and Age.\n
        Returns : Null"""
    print('Your name: \t '+name+'\nYour Age : \t '+str(age))


# 4) Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def calc_decade(years):
    """A divison of Years // 10 , to determine how many decades passed.\n
        Returns : Int"""
    return  years//10


def print_space():
    """Adds a line of  '-'  in the screen.\n
        Returns : Null"""
    print("----------------------------")


print_space()

name = new_name()
age = new_age()

print_space()

return_all(name,age)
print('Decades  : \t',calc_decade(age))

print_space()