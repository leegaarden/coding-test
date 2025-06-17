# 값 누적하기
n = int(input('n 입력: '))
s = 0

while n != 0:
    s += n
    n = int(input('n 입력: '))

print(s)