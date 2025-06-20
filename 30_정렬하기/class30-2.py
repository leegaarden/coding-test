# 버블 정렬
li = [5, 6, 7, 1, 4, 8, 9, 2, 3, 10]

for i in range(len(li)):
    print(li)
    for j in range(len(li)-i-1): # 마지막에는 맨 뒤의 두 개를 검사하기에 -1을 해야 함
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]