# 역삼각형 
n = int(input('n: '))

for i in range(n):
    print('*' * (n-i))

print() 

for i in range(n):
    print(' '*i, end='')
    print('*'*(n-i))