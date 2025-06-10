x= 3
y = 5

# 숫자와 문자 함께 출력하기 (1) 콤마와 형 변환
print(x, '과', y, '의 합은', x + y, '이다.') # 콤마
print(str(x) +'과' + str(y) + '의 합은' + str(x + y) + '이다.') # 형 변환

# 숫자와 문자 함께 출력하기 (2) end = ''
print(x, end = '')
print('과 ', end = '')
print(y, end = '')
print('의 합은', end = '')
print(x + y, end = '')
print('이다.')

# 숫자와 문자 함께 출력하기 (3) format()
print('{}과 {}의 합은 {}이다.'.format(x, y, x + y))