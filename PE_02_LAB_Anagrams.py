def word_count(a):
    sumch=[]
    for ch in range(len(a)):
        sumch.append(ord(a[ch]))
    return(sumch)

a1=input('Type the word 1:')
a2=input('Type the word 2:')
text1=a1.lower()
text2=a2.lower()


if sum(word_count(text1)) == sum(word_count(text2)):
    print('Anagrams')
else:
    print('Not anagrams')

