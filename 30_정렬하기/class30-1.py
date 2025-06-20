# 선택 정렬 
li = [5, 6, 7, 1, 4, 8, 9, 2, 3, 10]

for i in range(len(li)):
    print(li)
    m_index = i # 최소값의 인덱스
    for j in range(i, len(li)): # 시작 범위가 한 칸씩 뒤로 밀림
        if li[j] < li[m_index]:
            m_index = j
    li[i], li[m_index] = li[m_index], li[i] # 두 개의 자리 변경 