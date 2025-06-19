# 삼각형 
n = int(input('n: '))

for i in range(1, n+1):
    print('*'*i)

print()

for i in range(1, n+1):
    print(' '*(n-i), end='')
    print('*'*i)