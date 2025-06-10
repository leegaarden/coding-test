# 문자열 메소드

# 출력 지정: format(a, b, c, ...)
text = 'abcde {} {}'
print(text.format('ABC', 123))

# 대체하기
text = 'abcde ABCABC ABC'
print(text.replace('ABC', 'KKK'))

# 자르기
text = 'abcde ABCABC ABC'
a, b, c = text.split() 

print(a, b, c)

# 합치기
text = 'abcd e'
print('/'.join(text))

# 개수 확인하기
text = 'abcde ABCABC ABC'
print(text.count(a))
print(text.count('1'))
# print(text.count(1))

# 제거하기
text = 'abcde ABCABC ABCaaaa' 
print(text.strip('a'))
print(text.lstrip('a'))
print(text.rstrip('a'))

# 인덱스 찾기 
print(text.find('a'))
print(text.rfind('a'))
print(text.index('a'))
print(text.rindex('a'))

# 확인하기
text1 = 'ABCabc123'
text2 = '123.0'
text3 = 'ABC'
text4 = 'abc'

print(text2.isalnum())
print(text2.isdigit())
print(text3.isupper())
print(text4.islower())
print(text4.isalpha())

# 대소문자 만들기 
print(text1.upper())
print(text1.lower())

# 0 채우기
y = '2025'
m = '6'
d = '1'

print(y.zfill(4))
print(m.zfill(2))
print(d.zfill(1))