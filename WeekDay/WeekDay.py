#»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»#
#                                                       #
#   Given user inputs , determine which weekday it was  #
#                                                       #
#»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»#

def _Line(v_char,v_lengh):
    """Prints a line of chars , given chosen char  """
    c = ""
    for i in range(v_lengh):
        c = c + v_char
    return print("\n"+c+"\n")
 

def _tryAgain():
    """Gently asks the user to Try Again"""
    return print("\tIncorrect Value , please try again")


def getMonth():
    """Gets a valid Month digit"""
    v_Month = 0
    while True :
        try :
            v_Month   =   int(input("Enter Month :\t"))
            if v_Month == 0 or v_Month > 12 :
                raise   ValueError
        except ValueError :
            _tryAgain()
            continue
        break
    return v_Month


def getDay(a_Month):
    """Gets a valid value for Day , it verifies according to Month"""
    v_Day = 0

    while True :
        try :
            v_Day   =   int(input("Enter Day :\t"))
            if a_Month==1 or a_Month==3 or a_Month==5 or a_Month==7 or a_Month==8 or a_Month==10 or a_Month==12:
                if v_Day == 0 or v_Day > 31 :
                    raise   ValueError
            elif a_Month==3 or a_Month==4 or a_Month==6 or a_Month==9 or a_Month==11:
                if v_Day == 0 or v_Day > 30 :
                    raise   ValueError 
            elif a_Month==2:
                if v_Day == 0 or v_Day > 29 :
                    raise   ValueError
        except ValueError:
            _tryAgain()
            continue
        break
    return v_Day


def getYear():
    """Gets a valid Year"""
    v_year = 0

    while True :
        try :
            v_year    =   int(input("Enter Year :\t"))
            if v_year == 0 or v_year > 9999 :
                raise ValueError
        except ValueError:
            _tryAgain()
            continue
        break
    return v_year


def getLeap(a_year):
    """Returns if the given year is leap or not"""
    v_leap = False

    if (a_year % 4 == 0 and a_year % 100 > 0) or a_year % 400 == 0 :  
        v_leap = True
    else :
        v_leap = False
    return v_leap


def getCentury(a_year):
    """Returns century , digits given year"""
    return a_year // 100


def getYearDigits(a_year):
    """Returns year digits , given year"""
    return abs(a_year % 100)


def getValue(p_Month , p_Day , p_Year_digits ,p_Century , p_leap):
    """Returns a value  , given parameters :
        \nMonth , Day , Year Digits , Century , Leap"""
    Value   =   0

    Value   =   p_Year_digits + (p_Year_digits // 4)

    if p_Century == 18  : 
        Value += 2
    elif p_Century == 20  : 
        Value += 6

    if Month == 1 :
        if p_leap == False :
            Value += 1
    elif Month == 2 :
        if p_leap == True :
            Value += 3
        else    :
            Value += 4
    elif Month == 3 or Month == 11  :
        Value += 4
    elif Month == 4 or Month == 7   :
        Value += 0
    elif Month == 5 :
        Value += 2
    elif Month == 6 :
        Value += 5
    elif Month == 8 :
        Value += 3
    elif Month == 10 :
        Value += 1
    elif Month == 9 or Month == 12 :
        Value += 6

    return abs((Value+Day) % 7)


def returnDay(v_value):
    """Returns which day it was , given the value calculated past"""
    weekday = ""

    if  v_value == 1 : 
        weekday = "Sunday"
    elif    v_value == 2 : 
        weekday = "Monday"
    elif    v_value == 3 : 
        weekday = "Tuesday"
    elif    v_value == 4 : 
        weekday = "Wednesday"
    elif    v_value == 5 : 
        weekday = "Thursday"
    elif    v_value == 6 : 
        weekday = "Friday"
    elif    v_value == 0 : 
        weekday = "Saturday"
    return weekday


#»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»#
_Line("=",60)
print("\t\tDate format MM/DD/YYYY")
_Line("=",60)
Month           =   getMonth()
Day             =   getDay(Month)
Year            =   getYear()
_Line("#",60)
print("\tOn ",Month,"/",Day,"/",Year," it was a ",returnDay(getValue(Month,Day,getYearDigits(Year),getCentury(Year),getLeap(Year))),"!")
_Line("#",60)
#»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»#