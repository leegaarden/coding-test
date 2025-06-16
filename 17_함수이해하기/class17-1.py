# 함수 정의하기  인자값/리턴값
def aa():
    print('hi~')

def bb(x):
    for i in range(x):
        print('hello')

def cc():
    n = int(input('n: '))
    print(n*2)
    return n*2

def dd(x, y):
    print(x*y)
    return x*y

# 함수 호출하기
ref1 = aa()
ref2 = bb(3)
ref3 = cc()
ref4 = dd(3, 5)