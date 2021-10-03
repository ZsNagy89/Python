text = input("Enter your message: ")
shift=int(input('Number of shifting:'))
cipher = ''
for char in text:
    if ord(char) in range(65,91):
        if ord(char)+shift >90:
            code = ((ord(char)+shift)-90)+64
        else:
            code = ord(char) + shift
    elif ord(char) in range(97,123):
        if ord(char)+shift >122:
            code = ((ord(char)+shift)-122)+96
        else:
            code = ord(char) + shift
    else:
        code = ord(char)
    cipher += chr(code)

print(cipher)
