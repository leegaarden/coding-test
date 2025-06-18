# 평균 이상 개수 구하기
# 여러 개의 숫자를 입력 받아 평균을 구하고
# 평균 이상의 숫자 개수 구하기

num = list(map(int, input('숫자 입력: ').split()))

avg = sum(num) / len(num)
check = 0
for i in num:
    if i >= avg:
        check += 1

print('avg: ', avg)
print('check: ', check)