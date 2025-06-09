a = input("숫자를 입력하세요: ")
print(a + a)
# a를 숫자로 입력 받았지만, 파이썬은 이를 문자로 저장함

b = int(input("숫자를 입력하세요: "))
print(b + b)
# 문자가 된 b를 int형으로 변환함

num = 5.0
# range(num) # range 함수는 인자값으로 정수를 받아야 함
range(int(num))

c = int(a)
d = float(a)
print(type(a))
print(type(b))
print(type(c))
print(type(d))