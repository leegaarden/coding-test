# 반올림: round(a) -> a를 반올림, round(a, b) -> a를 소수점 b자리 까지 반올림
print(round(3.33))
print(round(6.66))
print(round(3.33, 1))

# 절대값: abs(a)
print(abs(3))
print(abs(-3))

# 제곱: pow(a, b)
print(pow(3, 2))
print(3 ** 2)

# 나눗셈: divmod(a, b) -> 몫과 나머지를 모두 반환
x, y = divmod(7,2)
print(x) # 7 // 2 (몫)
print(y) # 7 % 2 (나머지)

# 최대값: max(a, b, c, ...)
print(max(1,4, 3, 10))

# 최소값: min(a, b, c, ...)
x, y = divmod(7,2)
print(min(1,4, 3, 10))

# 합: sum(집합 형태) 
print(sum([1,4, 3, 10]))