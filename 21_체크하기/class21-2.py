# 숫자 체크
# 5개의 숫자를 입력 받아 리스트를 만들고, n을 입력받아 리스트 값에 n이 있는지 확인 

li = list(map(int, input('li: ').split()))
n = int(input('n: '))

check = False 

for i in li:
    if i == n:
        check = True

print(check)

# print(n in li)