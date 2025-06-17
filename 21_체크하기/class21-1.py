# 문자 체크
# 긴 문장과 한 문자를 입력받아 긴 문장 안에 문자가 포함 되어 있는지 확인 
text = input('text: ')
t = input('t: ')

# print(t in text

check = False

for i in text:
    if i == t:
        check = True
print(check)