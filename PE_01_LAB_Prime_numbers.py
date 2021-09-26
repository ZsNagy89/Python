def is_prime(num):
    list=[]
    for num in range(2,num+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                list.append(num)
    print(list)

is_prime(20)
