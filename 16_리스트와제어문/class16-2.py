# 리스트와 if문
li = [7, 5, 4, 9, 6]

# i가 인덱스인 경우 
for i in range(len(li)):
    if i%2 == 0:
        print(li[i])

print()

# i가 li의 값 자체인 경우 
for i in li:
    if i%2 == 0:
        print(i)