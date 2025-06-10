# 문자열 슬라이스
text = 'abcde fgh ijk' # 공백도 인덱스에 포함해야 함

print(text[2:5]) # 시작하려는 문자의 인덱스:자르고 싶은 인덱스 +  1
print(text[-5:-1]) # 뒤에서 부터 셀 경우 자르고 싶은 인덱스의 -1을 해주면 됨
print(text[5:])
print(text[:5])
print(text[:])
print(text[0:8:2]) # 0번 인덱스에서 7번 인덱스를 범위로 2개씩 띄우며 가져옴
print(text[8:0:-2]) # 뒤에서 부터 타고 와야 하기에 앞 인덱스가 더 커야 함
print(text[::-1]) # 처음부터 끝까지 문자열을 뒤집어서 