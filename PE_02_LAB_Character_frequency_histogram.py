from os import strerror

name=input('Please give me the file\'s name.')
try:
    cnt = 0
    dicty={}
    text = open(name, "rt")
    content = text.read()
    for i in content:
        if i.isalnum() == True:
            cnt += 1
            if i not in dicty.keys():
                dicty[i]=1
            else:
                dicty[i]+=1
    text.close()
    print("\n\nLetters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))

def letter_hist():
    for key in sorted(dicty.keys()):
        print(key, "-->", dicty[key])

letter_hist()


