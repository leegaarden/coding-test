# 튜플 만들기
tu = () 
tu = tuple()

# 튜플 인덱스
tu = ('a', 'b', 'c')

tu[0]
tu[1]
tu[2]

# tu[2] = 'd' # 변경이 불가능 하기에 에러 발생 

# 튜플 활용
tu.index('a') # 위치 확인하기
'b' in tu # 확인하기 -> True
'bb' in tu # 확인하기 -> False 
len(tu) # 전체 개수
tu.count('a') # a의 개수 

num = (5,7, 9)
n1, n2, n3 = num # 변수 할당하기, 반드시 서로 개수가 같아야 함 다를 경우 에러 발생 

a = 'hello'
b = 'world'
(a, b) = (b, a) # 값 교환하기

li = ['a', 'b', 'c', 'd', 'e', 'f']
li_tu = tuple(li) # 리스트 -> 튜플
print(li_tu)

tu = ('a', 'b', 'c')
tu_li = list(tu)
print(tu_li)