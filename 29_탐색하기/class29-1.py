# 선형 탐색 
li = [1, 5, 4, 3, 10, 2, 6, 7, 8, 9]
n = int(input('n(1 - 10): '))

for i in range(len(li)):
    if n == li[i]:
        print(i)
        break