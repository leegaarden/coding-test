# 리스트 분리하기
li = list(input('문자 입력: ').split())

up = []
low = []

for i in li:
    if i.isupper():
        up.append(i)
    if i.islower():
        low.append(i)

print(up)
print(low)