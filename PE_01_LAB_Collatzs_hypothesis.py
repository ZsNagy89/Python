c0=int(input("Take any non-negative and non-zero integer number: "))
steps=0               #stop parameter 
while c0!=1:
    if c0%2==0:
        c0=c0/2
        steps+=1
        print(int(c0))
    else:
        c0=3*c0+1
        steps+=1
        print(int(c0))
print("Steps=",steps)
