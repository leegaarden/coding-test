# n의 모든 배수 구하기 단 100 이하로 
n = int(input('n 입력: '))

for i in range(1, 101):
    if i%n ==0:
        print(i)