# 등차수열 
# 필요한 값: 맨 앞의 숫자, 더할 숫자, 몇 번째 항을 구할 것인가
a = int(input('맨 앞의 숫자 a: '))
b = int(input('더할 숫자 b: '))
n = int(input('몇 번째 항을 구할 것인가 n: '))

for i in range(n-1): # 예시로 5항을 구하려면 4번 계산이 되기에 n-1 -> 0, 1, 2, ... n-2
    a += b

print(a)