def day_of_year(year,month,day):
    months=range(month)
    for i in range(month):
        days_vector=[]
        if year%4==0:                                 #maybe Leap year
            if year%100==0 and year%400!=0:           #not a leap year
                if months[i] in x:
                    if months[i]==2:
                        test_days.append(28)
                    else:
                        test_days.append(30)
                else:
                    test_days.append(31)
            else:                                       #leap year
                if months[i] in x:
                    if months[i]==2:
                        test_days.append(29)
                    else:
                        test_days.append(30)
                else:
                    test_days.append(31)
        else:                                           #not a leap year
            if months[i] in x:
                if months[i]==2:
                    test_days.append(28)
                else:
                    test_days.append(30)
            else:
                test_days.append(31)
    del test_days[0]                       # delete the 0th item
    test_days.append(day)                  # add day number to elem
    sum(test_days)


x=(2,4,6,9,11)
test_days=[]
day_of_year(1989,2,10)
print(sum(test_days))
