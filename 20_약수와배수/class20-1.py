# 약수와 배수 판별
# 숫자를 입력받아 b가 a의 약수인지 확인 
a = int(input('a 입력: '))
b = int(input('b 입력: '))

if a % b == 0:
    print('b는 a의 약수입니다.')
else:
    print('b는 a의 약수가 아닙니다.')

# b가 a의 배수인지 확인 
a1 = int(input('a1 입력: '))
b1 = int(input('b1 입력: '))

if b1 % a1 == 0:
    print('b는 a의 배수입니다.')
else:
    print('b는 a의 배수가 아닙니다.')
 