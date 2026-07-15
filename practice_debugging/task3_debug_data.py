
while True:
    date = input("Enter the date (DD-MM-YYYY): ") # 2) Missing indentation
    test = date
    if len(test)== 10 and test[2]=="-" and test[5]=="-": # 1) Changed = to ==
        day = int(test[0:2])
        month = int(test[3:5]) # 6) Logic error
        year = int(test[6:])
        check_year = year>1900 and year<=2026 # 8) Changed to 2026
        check_month = month>=1 and month<=12 # 9) Changed or to and
        check_day_31 = day<=31 and (month in [1,3,5,7,8,10,12])
        check_day_30 = day<=30 and (month in [4,6,9,11]) # 10) Changed 31 to 30
        check_day_Feb = month == 2 and ((day<=29 and year%4==0) or day<=28) # 11) Changed 0 to 2
        if check_year: # 3) Added missing "_"
            if check_month:
                if check_day_31 or check_day_30 or check_day_Feb: # 5) Missing ":"
                    break
                else:
                    print("Error in day")
            else:
                print("Error in month") # 7) Changed to month and changed to year
        else:
            print("Error in year")
    else:
        print("Error in format") # 4) Missing "
print("Date accepted")
