# 약수 구하기 
# 숫자 n을 입력받아 n의 모든 약수 구하기

n = int(input('n 입력: '))

for i in range(1, n+1):
    if n%i ==0:
        print(i)