date=input('Please, write your birthday:')
lst=list(date)
suma=0
for i in range(len(lst)):
        suma+=int(lst[i])
if len(str(suma))>=2:
        suma2=list(str(suma))
        suma_f=int(suma2[0])+int(suma2[-1])
print(suma_f)
