#»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«#
#                                                                                                                                                                #
#   Given user inputs , determine which weekday it was                                                                                                           #
#                                                                                                                                                                #
#»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«#
while True :
    try :
        month   =   int(input("Enter Month \t"))
        if month == 0 or month > 12 :
            raise   ValueError
        break
    except ValueError :
        print("\tIncorrect Value , try again")
        pass

while True :
    try :
        day     =   int(input("Enter Day   \t"))
        if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
            if day == 0 or day > 31 :
                raise   ValueError
        elif month==3 or month==4 or month==6 or month==9 or month==11:
            if day == 0 or day > 30 :
                raise   ValueError 
        elif month==2   :
            if day == 0 or day > 29 :
                raise   ValueError
        break
    except ValueError:
        print("\tIncorrect Value , try again")
        pass
 
while True :
    try :
        year    =   int(input("Enter Year  \t"))
        if year == 0 or year > 9999 :
                raise ValueError
        break
    except ValueError:
        print("\tIncorrect Value , try again")
        pass

century_digits  =   year // 100
year_digits     =   abs(year % 100)
value           =   year_digits + (year_digits//4)

if (year % 4 == 0 and year % 100 > 0) or year % 400 == 0 :  
    Bissexto = True
else    :                                                   
    Bissexto = False

if      century_digits == 18  : value = value + 2
elif    century_digits == 20  : value = value + 6

if month == 1 :
    if Bissexto == False :
        value = value + 1    
elif month == 2 :
    if Bissexto == True :
        value = value + 3
    else    :
        value = value + 4
elif month == 3 or month == 11  :    
    value = value + 4
elif month == 4 or month == 7   :    
   value =  value + 0
elif month == 5 :   
    value = value + 2
elif month == 6 :   
    value = value + 5
elif month == 8 :   
    value = value + 3
elif month == 10 :   
    value = value + 1
elif month == 9 or month == 12 :   
    value = value + 6

value = abs((value+day) % 7)

if      value == 1 : weekday = "Sunday"
elif    value == 2 : weekday = "Monday"     
elif    value == 3 : weekday = "Tuesday"    
elif    value == 4 : weekday = "Wednesday"  
elif    value == 5 : weekday = "Thursday"   
elif    value == 6 : weekday = "Friday"     
elif    value == 0 : weekday = "Saturday"   

print("On ",month,"/",day,"/",year," it was a ",weekday)
#»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«#