# 약수의 개수 구하기
# n의 약수 개수구하기

# 1. check 변수에 저장 
n = int(input('n: '))

check = 0

for i in range(1, n+1):
    if n%i == 0:
        check+=1
        print(i)

print('약수의 개수: ', check)

# 2. 리스트에 약수 자체를 저장 
n = int(input('n: '))

li = []

for i in range(1, n+1):
    if n%i == 0:
        li.append(i)
        print(i)

print('약수의 개수: ', len(li))