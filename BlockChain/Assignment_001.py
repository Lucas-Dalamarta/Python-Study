# -*- coding: utf-8 -*-

# 1) Create two variables – one with your name and one with your age
global name , age

# 2) Create a function which prints your data as one string
def new_name():
    return  raw_input('Enter your name : ')


def new_age():
    return  int(raw_input('Enter your age : '))


# 3) Create a function which prints ANY data (two arguments) as one string
def return_all(name,age):
    print('Your name: \t '+name+'\nYour Age : \t '+age)


# 4) Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def calc_decade(years):
    return  years//10

def print_space():
    print("----------------------------")


print_space()

name = new_name()
age = new_age()

print_space()

return_all(name,str(age))
decades = calc_decade(int(age))

print('Decades  : \t'+str(decades))

print_space()