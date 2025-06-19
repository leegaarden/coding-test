# 행렬 만들기
li = [[1, 2, 3, 4,], [5, 6, 7, 8]]

for i in range(len(li)): # 2   i = 0, 1
    for j in range(len(li[i])): # 4   j = 0, 1, 2, 3
        print(li[i][j], end='')
    print()