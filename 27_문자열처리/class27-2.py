# 대소문자 바꾸기
text = input('text: ')

for i in text:
    if i.isupper():
        print(i.lower(), end='')
    elif i.lower():
        print(i.upper(), end='')
    else: 
        print(i, end='')