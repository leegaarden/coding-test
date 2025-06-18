# OX 개수 구하기
# text 입력받아 o와 x의 개수 구하기 
text = list(input('text: '))

'''print(text.count('o'))
print(text.count('x'))
'''

o_count = 0
x_count = 0

for i in text:
    if i == 'o':
        o_count += 1
    elif i == 'x':
        x_count += 1

print(o_count)
print(x_count)