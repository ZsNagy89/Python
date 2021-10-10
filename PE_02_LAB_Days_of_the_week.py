class WeekDayError(BaseException):
    pass

class Weeker:
    dic={'Mon':0,'Tue':1,'Wed':2,'Thu':3,'Fri':4,'Sat':5,'Sun':6}
    dic2={0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
    def __init__(self, day):
        self.day=day
        self.day_nm=Weeker.dic[day]

    def __str__(self):
        return Weeker.dic2[self.day_nm]

    def add_days(self, n):
        self.n=n
        self.day_nm+=self.n
        if self.day_nm > 6:
            while self.day_nm not in range(7):
                self.day_nm-=6

    def subtract_days(self, m):
        self.m=m
        self.day_nm-=self.m
        if self.day_nm < 0:
            while self.day_nm not in range(7):
                self.day_nm+=6
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except:
    print("Sorry, I can't serve your request.")
