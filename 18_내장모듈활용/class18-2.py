# random 모듈 
import random

print(random.randint(1, 5)) # 범위 내의 정수 랜덤값 생성(보통의 파이썬 범위와 달리 5도 포함)
print(random.random()) # 0 부터 1 사이의 랜덤값 생성  

li = ['a', 'b', 'c', 'd', 'e']
print(random.choice(li)) # 리스트 값 중 하나 랜덤으로 뽑기
print(random.sample(li, 3)) # 리스트에서 랜덤으로 3개 뽑기 
random.shuffle(li) # 리스트 순서 랜덤으로 섞기 
print(li)