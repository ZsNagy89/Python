in_find=input('Please write a text:')
in_text=input('Please write a word:')
text=in_text.lower()
word=in_find.lower()

if text.find(word)!=-1:
    print('Yes')
else:
    print('No.')
