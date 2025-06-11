# while 문
print('a가 0보다 크거나 같으면 실행, 아니면 정지')

a = int(input('a를 입력하세요: '))

while a >= 0:
    print('실행')
    a = int(input('a를 입력하세요: '))

# 무한 루프
'''
a = 10

while a >= 0:
    print('실행')


# n번 반복하기
n = int(input('n을 입력하세요: '))

while n: # 숫자만 들어갈 경우 양수일 때는 true, 음수일 때는 false
    print(n)
    n = n - 1

# ~까지 반복하기 (1) 1 ~ 10까지 반복하기
n = 1

while n <= 10:
    print(n)
    n += 1

# ~까지 반복하기 (2) yes를 입력하면 반복하기 
text = 'yes'

while text == 'yes':
    text = input('yes입력시 반복: ')

print('end')
'''
# ~까지 반복하기 (3) e또는 E가 입력될 때까지 반복하기
text = input('e또는 E 입력 시 종료')

while text != 'e' and text != 'E':
    text = input('e또는 E 입력 시 종료 ')
    
print('end')