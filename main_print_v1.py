# 변수 선언
name = "홍길동"
age = 21
score = 95.5

# 1. 기본 출력
print("Hello, Python!")

# 2. 여러 값 출력 (콤마로 구분 → 자동 띄어쓰기)
print("Name:", name, "Age:", age, "Score:", score)

# 3. f-string (가장 많이 쓰임, Python 3.6+)
print(f"My name is {name}, I am {age} years old, score: {score}")

# 4. format() 함수
print("My name is {}, I am {} years old, score: {}".format(name, age, score))

# 5. % 포맷팅 (옛 방식)
print("My name is %s, I am %d years old, score: %.1f" % (name, age, score))

# 6. sep 옵션 (구분자 지정)
print("2025", "09", "29", sep="-")

# 7. end 옵션 (줄바꿈 대신 다른 문자)
print("Hello", end=" ")
print("World!")

# 8. 여러 줄 출력
print("""여러 줄
문자열을
한 번에 출력""")

# 9. 이스케이프 문자
print("탭\t구분, 줄바꿈\n다음 줄, 따옴표 \"인용\"")

# 10. 소수점 자리수 / 정렬
pi = 3.14159265
print(f"pi = {pi:.2f}")
print(f"[{name:>10}]")   # 오른쪽 정렬
print(f"[{name:<10}]")   # 왼쪽 정렬
print(f"[{name:^10}]")   # 가운데 정렬

# 11. 천 단위 콤마
money = 1234567
print(f"금액: {money:,}원")
