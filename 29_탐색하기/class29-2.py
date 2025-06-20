# 이진 탐색 
li = [1, 3, 5, 6, 8 , 9, 13, 15, 17, 19]
n = int(input('1, 3, 5, 6, 8 , 9, 13, 15, 17, 19: '))

s_index = 0 # 처음 인덱스 
e_index = len(li) - 1 # 끝 인덱스 

while s_index <= e_index: # 간격이 좁혀질 때까지 반복 
    m_index = (s_index + e_index) // 2 # 중간 인덱스 (int만 들어갈 수 있기에 //를 해서 몫만 갖고 오기)
    if n < li[m_index]: 
        e_index = m_index - 1 # 숫자가 중간 값보다 작았을 경우, 중간보다 앞에 범위만 검사 
    elif n > li[m_index]:
        s_index = m_index + 1 # 숫자가 중간 값보다 컸을 경우, 중간보다 뒤에 범위만 검사 
    else: # 처음 고른 숫자가 바로 중간 값일 때 
        print(m_index)
        break
