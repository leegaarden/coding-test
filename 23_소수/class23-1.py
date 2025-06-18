# 소수 판별하기 
n = int(input('n: '))

# 첫 번째 방식 
check = 0
for i in range(1, n+1):
    if n%i == 0:
        check += 1

if check == 2:
    print(n, '은 소수입니다.')
else:
    print(n, '은 소수가 아닙니다.')

# 두 번째 방식 
check = True
for i in range(2, n):
    if n%i == 0:
        check = False

print(check)

# 두 번쨰 방식의 문제점: 1은 소수가 아닌데 소수로 판별됨 
# 개선 

if n < 2:  # 2보다 작은 수는 소수가 아님
    check = False
else:
    check = True
    for i in range(2, n):
        if n % i == 0:
            check = False
            break  # 약수를 찾으면 더 이상 확인할 필요 없음

print(check)