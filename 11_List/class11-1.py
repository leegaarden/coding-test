# 리스트 만들기 
li = []
li = list()

# 리스트 인데스 
li = ['a', 'b', 'c']

print(li[0])
print(li[1])
print(li[2])

li[1] = 'd'
print(li)

# 리스트 활용
li = ['a', 'b', 'c', 'd', 'e']

li.index('d') # 위치 찾기

li.append('f') # 맨 끝에 추가하기
li.insert(0, 'aa') # 특정 인덱스에 추가하기

li.remove('aa') # 삭제하기
del li[2] # 특정 인덱스 값 삭제하기 

'b' in li # b가 있는지 확인하기 -> True
'r' in li # r이 있는지 확이나기 -> False

len(li) # 전체 개수 
li.count('a') # li에서 a의 개수 구하기 

num = [1,2,3,4,5,6,7,8,10,9]

sum(num) # 합 구하기
min(sum) # 최소값 구하기
max(sum) # 최대값 구하기 

num.reverse() # 역순 만들기 -> 9,10,8,7,6,5,4,3,2,1

num.sort() # 오름차순 정리 -> 1,2,3,4,5,6,7,8,9,10
num.sort(reverse=True) # 내림차순 정리 -> 10,9,8,7,6,5,4,3,2,1