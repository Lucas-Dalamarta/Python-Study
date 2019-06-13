global a , b , choice


def _sum(a,b):
    """Returns a + b"""
    return  print("\t "+str(a)+" + "+str(b)+" = "+str(a+b))


def _sub(a,b):
    """Returns a - b"""
    return  print("\t "+str(a)+" - "+str(b)+" = "+str(a-b))


def _div(a,b):
    """Returns a / b"""
    return  print("\t "+str(a)+" / "+str(b)+" = "+str(a/b))


def _mul(a,b):
    """Returns a * b"""
    return  print("\t "+str(a)+" X "+str(b)+" = "+str(a*b))


def _Line(o):
    """Prints a line of chars , given chosen char """
    c = ""
    for i in range(40):
        if o == "=" :
            c = c + "="
        elif o == "-" :
            c = c + "-"
        elif o == "*" :
            c = c + "*"
        else :
            c = c + " "

    return print(c)

def menu():
    _Line("=")
    print("\tEnter [1] to   Sum ")
    print("\tEnter [2] to   Sub ")
    print("\tEnter [3] to   Div ")
    print("\tEnter [4] to   Mul ")
    _Line("=")
#-------------------------------------
while True:
    choice = 0

    a = int(input("Enter a number :\t"))
    b = int(input("Enter another number :\t"))

    menu()

    choice = int(input("Option :\t"))

    if choice   == 1:
        _sum(a,b)
    elif choice == 2:
        _sub(a,b)
    elif choice == 3:
        _div(a,b)
    elif choice == 4:
        _mul(a,b)
    
    _Line("*")
    choice = int(input("Do you want to go again ? [0/1] \t"))
    _Line("*")
    
    if choice == 0:
        break
    else:
        pass
