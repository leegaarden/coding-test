# 범위 내의 소수 구하기 
# a의 값을 입력 받아 1 - a 사이의 모든 소수값 구하기 (a > 0)

# 직접 해본 방식 
a = int(input('a: '))
li = []

for i in range(2, a+1): # 1은 소수가 아니므로 2부터 검사 
    check = True
    for j in range(2, i):
        if i%j == 0: # 소수가 아닌 경우
            check = False
    if check:
        li.append(i)

print(li)

# 강의 방식
a = int(input('a: '))
li = []

for n in range(2, a+1):
    check = True
    for i in range(2, n):
        if n%i == 0:
            check = False
    if check:
        li.append(n)

print(li)