# 숫자 활용 (합, 평균, 최소값, 최대값, 중간값)
num = list(map(int, input('숫자 입력: ').split()))

num.sort()

print('합: ', sum(num))
print('평균: ', sum(num)/len(num))
print('최소값: ', num[0])
print('최소값: ', min(num))
print('최대값: ', num[len(num) - 1])
print('최대값: ', max(num))
print('중간값: ', num[len(num)//2])