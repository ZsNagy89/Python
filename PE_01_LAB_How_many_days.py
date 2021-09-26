def is_year_leap(year):
    for i in range(len(year)):
        if year[i]%4==0:
            if year[i]%100==0 and year[i]%400!=0:
                test_years.append(False)
            else:
                test_years.append(True)
        else:
            test_years.append(False)
    

test_years=[]
year=(1900, 2000, 2016, 1987)
is_year_leap(year)
print(test_years)
#How many days
def days_in_month(year, month):
    for i in range(len(month)):
        if month[i] in y:
            if test_years[i]== True:
                if month[i] in x:
                    if month[i]==2:
                        test_days.append(29)
                    else:
                        test_days.append(30)
                else:
                    test_days.append(31)
            else:
                if month[i] in x:
                    if month[i]==2:
                        test_days.append(28)
                    else:
                        test_days.append(30)
                else:
                    test_days.append(31)
        else:
            test_days.append(None)

month=(2, 15, 1, 11)
y=(1,2,3,4,5,6,7,8,9,10,11,12)
x=(2,4,6,9,11)
test_days=[]
days_in_month(year, month)
print(test_days)
