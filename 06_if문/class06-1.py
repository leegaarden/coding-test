# if 문
num = int(input("숫자를 하나 입력하세요: "))

if num > 0:
    print(("{}은 양수입니다.").format(num))

# if ~ else 
if num % 2 == 0: 
    print(("{}은 짝수입니다.").format(num))
else:
    print(("{}은 홀수입니다.").format(num))

# if ~ elif
age = int(input("나이를 입력해 주세요: "))

if age <= 7:
    print("유아입니다.")
elif age <= 19:
    print("청소년입니다.")
elif age >= 20:
    print("성인입니다.")

# if ~ elif ~ else
text = input("알파벳 입력: ")

if text.isupper():
    print("대문자")
elif text.islower():
    print("소문자")
else:
    print("대소문자 구분 불가능")