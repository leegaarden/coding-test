# 주사위
a = int(input('a: '))
b = int(input('b: '))
n = int(input('n: ')) # a와 b를 합해서 나온 값 

for i in range(1, a + 1):
    for j in range(1, b + 1):
        if i + j == n: # 합한 값이 n인 수만 출력 
            print(i, j)