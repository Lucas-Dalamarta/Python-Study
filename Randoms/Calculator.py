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


def _Line(v_char):
    """Prints a line of chars , given chosen char  """
    c = ""
    for i in range(40):
        c = c + v_char
    return print(c)


def _Get_A():
    """Returns A value , but only if it's a valid integer"""
    a_value = 0

    while True:
        try:
            a_value = int(input("Enter a value for A :\t"))
            if a_value <= 0 :
                raise ValueError
        except  ValueError:
            print("Incorrect value , try again !")
            continue
        break    
    return a_value


def _Get_B():
    """Returns B value , but only if it's a valid integer"""
    b_value = 0

    while True:
        try:
            b_value = int(input("Enter a value for B :\t"))
            if b_value <= 0 :
                raise ValueError
        except  ValueError:
            print("Incorrect value , try again !")
            continue
        break
    return b_value


def menu():
    """Displays options to use calculator"""
    _Line("=")
    print("\tEnter [1] to   Sum ")
    print("\tEnter [2] to   Sub ")
    print("\tEnter [3] to   Div ")
    print("\tEnter [4] to   Mul ")
    _Line("=")


def main():
    """Old habits ..."""
while True:
    choice = 0
        
    a = _Get_A() 
    b = _Get_B()

    menu()

    choice = int(input("Option :\t"))
    
    _Line("*")

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
    
    if choice == 1:
        continue
    else:
        break


#-------------------------------    EXEC    --------------------
_Line(":")
main()
print("\tApplication Ended !")
_Line(":")
#---------------------------------------------------------------