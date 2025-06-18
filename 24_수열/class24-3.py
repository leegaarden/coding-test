# 피보나치 수열 
a, b = map(int, (input('처음의 두 숫자 입력 a, b: ').split())) # 처음의 두 숫자 입력 
n = int(input('몇 번째 항을 구할 것인가 n: '))

for i in range(n-2):
    c = a+b
    a = b # 한 항씩 당겨지기 
    b = c # 한 항씩 당겨지기 

print(b)