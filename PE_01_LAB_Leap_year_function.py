#Leap year function
def is_year_leap(year):
    for i in range(len(year)):
        if year[i]%4==0:
            if year[i]%100==0 and year[i]%400!=0:
                test_results.append(False)
            else:
                test_results.append(True)
        else:
            test_results.append(False)
    

test_results=[]
year=(1900, 2000, 2016, 1987)
is_year_leap(year)
print(test_results)
