# 딕셔너리 만들기
dic = {}
dic = dict()

# 딕셔너리 특징 : 키와 값으로 이루어짐 
dic = {'kor':80, 'eng':90, 'math':77}
dic['kor']

dic['kor'] = 85 # 값 변경하기 
# dic[0] # 딕셔너리를 키와 값으로 이루어져 있기에 인데스로 출력하면 에러 발생 
dic['sci'] = 78  # 원래 없던 키 값을 넣으면 추가가 됨 

# 딕셔너리 활용 
del dic['math'] # 키 삭제하기 
dic.clear() # 전체 삭제 
'eng' in dic # 확인하기(키 기준으로) -> True, False
len(dic) # 전체 개수 (키들의 길이)

dic = {'kor':80, 'eng':90, 'math':77}

print(dic.keys()) # 모든 키 얻기
print(list(dic.keys())) # 모든 키를 리스트로 얻기
print(tuple(dic.keys())) # 모든 키를 튜플로 얻기

print(dic.values()) # 모든 값 얻기 
print(list(dic.values())) # 모든 값을 리스트로 얻기
print(tuple(dic.values())) # 모든 값을 튜플로 얻기

print(dic.items()) # 모든 순서쌍 얻기
print(list(dic.items())) # 모든 순서쌍을 리스트로 얻기
print(tuple(dic.items())) # 모든 순서쌍을 튜플로 얻기

print(tuple(dic))
print(list(dic))
print(set(dic))

li = ['ab', 'cd', 'ef']
print(dict(li)) # 위와 같이 순서가 값들이 일정하게 있는 리스트는 딕셔너리로 만들 수 있음
li = li = ['ab', 'cd', 'eff']
# print(dict(li)) # 순서가 일정하지 않으면 에러가 뜸 

li = [['a', 1], ['b', 2], ['c', 3]]
print(dict(li)) # 순서가 일정하면 이중 리스트도 딕셔너리로 가능 
li = [['a', 1], ['b', 2], ['c', 3, 4]]
# print(dict(li)) # 순서가 일정하지 않으면 딕셔너리로 만들 수 없음  