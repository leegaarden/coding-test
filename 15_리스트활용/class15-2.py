# 숫자 하나씩 입력 받기
li3 = []

li3.append(int(input('숫자 입력: ')))
li3.append(int(input('숫자 입력: ')))
li3.append(int(input('숫자 입력: ')))

print(li3)

# 숫자 여러 개 입력 받기
li4 = list(map(int, input('숫자 입력: ').split()))
print(li4)
# 과정 풀어서 서술 
a = input('숫자 입력: ').split()
b = map(int, a)
c = list(b)