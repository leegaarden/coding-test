# 세트 만들기 
se = set()
# se = {} # 비어있는 상황에서 {}로 만들면 set가 아닌 딕셔너리가 만들어짐 

# 세트 특징: 순서와 중복이 없음 
a = {2, 4, 6, 8, 1}
print(a)

b = {7, 2, 2, 3, 3, 3, 6, 1}
print(b)

# print(a[0]) # 순서가 없기에 인덱스로 호출하면 에러

# 세트 활용하기 
a.add(5) # 추가하기 
a.remove(5) # 삭제하기
1 in a # 1이 있는지 확인하기 True, False
len(a) # 전체 개수(길이 구하기)
sum(a) # 합 구하기 
min(a) # 최소값 찾기 
max(a) # 최대값 찾기
list(a) # 리스트로 만들기
tuple(a) # 튜플로 만들기

# 집합 처럼 연샨하기 
print(a&b) # 교집합 
print(a|b) # 합집합 
print(a-b) # 차집합
print(a^b) # 대칭 차집합 -> a|b - a&b