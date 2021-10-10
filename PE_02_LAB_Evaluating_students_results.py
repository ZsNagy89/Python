#file's name: student_data.txt
from os import strerror

name=input('Please give the data file\'s name.')
try:
    dicty={}
    text = open(name, "rt")
    content = text.readlines()
    words=[]
    keys=[]
    values=[]
    dicty={}

    for i in range(len(content)):
        words.append(content[i].split())

    for j in range(len(content)):
        keys.append(words[j][0]+' '+words[j][1])
        values.append(float(words[j][2]))
    
    for k in range(len(keys)):
        if keys[k] not in dicty.keys():
            dicty[keys[k]]=values[k]
        else:
            dicty[keys[k]]+=values[k]
    print(dicty)

    text.close()

except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))
