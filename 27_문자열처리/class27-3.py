# 이름 찾기
name = ['김철수', '김영희', '홍김동', '이정원', '문자열처리']

for i in name:
    if '김' in i:
        print(i)

print()

for i in name:
    if i[0] == '김': # 성이 김인 경우만 
        print(i)