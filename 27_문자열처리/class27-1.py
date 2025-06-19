# 띄어쓰기 없애기 
text = input('text: ')

for i in text:
    if i != ' ': # 공백이 아닌 것만 출력 
        print(i, end='')