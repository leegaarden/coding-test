# range() 연습

print(range(5))
print(list(range(5)))
print(list(range(1, 11)))
print(list(range(3, 10, 3)))
print(list(range(5, 0, -1)))
print(list(range(10, -11, -5)))

# for문
for i in range(10):
    print(i)

# 1에서 n까지 출력
n = int(input('n: '))

for i in range(1, n+1):
    print(i)

# a에서 b까지 출력
a, b = map(int,input('a b: ').split())

for i in range(a, b+1):
    print(i)

# n에서 0까지 출력 
n = int(input('n: '))

for i in range(n, -1, -1): 
    print(i)