def read_int(prompt, min, max):
    min=-10
    max=10
    lst=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
    try:
        prompt=int(input('IRj szamot:'))
        assert prompt in lst
    except ValueError:
        print("Error: Wrong input!")
    except AssertionError:
        print("Error: the value is not within permitted range (min..max)")
    return prompt
    
v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
