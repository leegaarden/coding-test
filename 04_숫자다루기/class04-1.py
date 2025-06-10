# 한 줄에 하나씩 숫자 입력 받기
a = int(input("a를 입력해 주세요: "))
b = int(input("b를 입력해 주세요: "))
c = int(input("c를 입력해 주세요: "))

print(a, b, c, a + b + c)

# 한 줄에 여러 개의 숫자 입력 받기
A, B, C = map(int, input("A, B, C 값을 입력해 주세요: ").split())

print(A, B, C, A + B + C)

# 문자1.split('문자2'): 문자2를 기준으로 문자1을 자른다
text = input('날짜 입력 yyyy.mm.dd ')
y, d, m = text.split('.')

print(y, d, m)

# map(함수, 집합 형태)
a, b, c = map(int, ['1', '2', '3'])

print(a, b, c, a + b + c)

text = input('a b c 입력')
text= text.split() # 공백을 기준으로 잘라주기
a, b, c = map(int, text)

print(a, b, c, a + b + c)