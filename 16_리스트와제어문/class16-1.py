# for문으로 리스트 값 추가 
li = []

for i in range(5):
    li.append(int(input('숫자 입력: ')))

# for문으로 리스트 값 출력 
for i in range(len(li)):
    print(li[i])

# 좀 더 간단하게: 리스트 통으로 넣기
for i in li:
    print(i)