# 피라미드
n = int(input('n: '))

for i in range(n):
    print(' '*(n-i-1), end='')
    print('*'*(i*2+1))