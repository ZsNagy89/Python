class Timer:
    def __init__(self, hours=0, minutes=0,seconds=0):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

    def __str__(self):
        return str(self.hours) + ':' + str(self.minutes) + ':' + str(self.seconds)

    def next_seconds(self):
        self.seconds+=1
        if self.seconds >= 60:
            self.seconds-=60
            self.minutes+=1
            if self.minutes >= 60:
                self.minutes-=60
                self.hours+=1
                if self.hours >= 24:
                    self.hours-=24

    def prev_seconds(self):
        self.seconds-=1
        if self.seconds < 0:
            self.seconds+=60
            self.minutes-=1
            if self.minutes < 60:
                self.minutes+=60
                self.hours-=1
                if self.hours < 0:
                    self.hours+=24

timer = Timer(23, 59, 59)
print(timer)
timer.next_seconds()
print(timer)
timer.prev_seconds()
print(timer)
