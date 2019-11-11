# 1. 문자열 만드는 방법
# 1) 큰따옴표로 감싸기
# 2) 작은따옴표로 감싸기
# 3) 큰따옴표 세개로 감싸기
life = """Life is too short"""
print(life)
# 4) 작은따옴표 세개로 감싸기
python = '''You need python'''
print(python)

# 2. 문자열 만드는 방법 골고루 활용하기
# 1) 문자열안에 큰따를 문자로 인식하고 싶은 경우 작따로 감싸기
singlechar = "Python's favorite food is perl"
print(singlechar)
# 2) 반대
doublechar = '"Pyton is very eaxy" he says'
print(doublechar)
# 3) 작따나 큰 따앞에 역슬래쉬를 붙인다.
food = "Python\'s favortie food is perl"
say = "\"python is very easy.\" he says"

#3. 여러줄인 문자열을 변수에 대입하고 싶을 때
#1) 줄바꿈 서식문자 = 이스케이프 코드 이용
#2) 작따 세개 or 큰따 세개 이용
multiline = ''' Life is toot short
You need python'''
print(multiline)
multiline = """
Life is too short
You need python"""
print(multiline) # 따옴표를 연달아서 쓰는 것이 깔끔하다.

# 이스케이프 코드 종류
# 1) \n : 줄바꿈
# 2) \t : 탭으로 띄어쓰기 줄때 사용
# 3) \\ : 문자 역슬래쉬를 그대로 표현할 때 사용
# 4) \' \"작따를 표현할 때, 큰따를 표현할 때 사용

# 5. 문자열 연산하기
# + : 문자열 이어붙이기
head = "python"
tail = "is fun!"
print(head + tail)
# * 문자열 반복해서 만들기
a = "python"
print(a * 2)

#6. 문자열 길이 구하기 = len()
a = "Life is too short"
print(len(a))

# 7. 문자열 인덱싱과 슬라이싱
# 1) 문자열 인덱싱 : 문자열에서 특정부분 문자 뽑아낸다.
a = "Life is too short, You need Phton"
print(a[3])
print(a[0])
# a[-1]은 뒤에서부터 첫번째 문자를 의미한다.
print(a[-1])
#a[0] = a[-0]
print(a[-0])
# 뒤에서부터 두번째 문자
print( a[-2])
# 뒤에서부터 다섯번째 문자
print(a[-5])

# 2) 문자열 슬라이싱 : 문자열 일부분만 뽑아내는 것이다.
# 1. 첫번째 숫자를 생략하면 처음부터 출력
# 2. 끝 숫자를 생략하면 끝 까지 출력
# 3. 둘다 생략하면 처음부터 끝까지 출력
# 4. 시작 문자 포함 끝 문자 미포함 하여 출력
# 인덱스 0번째 문자부터 3번째 문자까지 출력
print(a[0:4])

#공백 역시도 문자로 취급된다.
print(a[0:5])
# 슬라이싱 에서도 마이너스 기호를 나눌 수 있다.
a = 'Life is short, You need Python'


# 인덱싱과 슬라이싱은 튜플과 리스트에서도 사용된다.
#Pithon이라는 문자열을 Python이라는 문자열로 바꾸려면?
# p[1] = 'y'는 오류가 발생한다. 왜냐하면 문자열의 요소값은 바꿀 수 없다.
p = 'Pithon'
print(p[0] + 'y' + p[2:])

#8. 문자열 포매팅
# 문자열에서 일정 부분만 바꿔서 출력하고자 할 때 사용할 수 있다.
# 포매팅 문자 사용 : %d, %s 등
# 한번에 여러값 대입하기
print(" I eat %d apples and i sick for %s days " %(3, 'three'))
# 포맷팅 문자 여러개 존재한다.
# 1) %d : 10진수 정수
# 2) %f : 실수
# 3) %o : 8진수 정수
# 4) %x : 16진수
# 5) %c : 문자 한개
# 6) %s : 문자열
# 7) %% : 문자 % 나타낼때
print("Error is %d%%" % 98)
# -----------------
# 8) %s 를 사용하면 어떤 값이든 나타낼 수 있다. 단 문자열로 바꿔서 나타낸다.

# 3) 포맷코드와 숫자 함께 사용하기
#1.  = 정렬과 공백
#오른쪽 정렬
hi = 'hi'
print("%10s" % hi)
# 왼쪽 정렬
print("%-10s" % hi)

# 2. 소수점 표현하기
a = 3.1234556
print("%10.2f" % a)

# 4) format 함수를 사용한 포매팅
print( " I eat {0} apples ". format(3))
print(" I eat {0} apples so i sick for {1} days".format(3, 'ten'))
count = 3
days = 'three'
print(" I eat {0} apples so i sick for {1} days".format(count, days))

# 4).5 이름으로 넣기
print(" I eat {number} apples so i sick for {day}days".format(number = 3, day = 3))
# 6. 인덱스와 이름 혼용해서 넣기
print(" I eat {0} apples so i sick for {day} days".format(3, day = 'ten'))
# 7. 왼쪽 정렬
print("{0:<10}".format('hi'))
# 8. 오른쪽 정렬
print("{0:>10}".format('hi'))
# 9. 가운데 정렬
print("{0:^10}".format('hi'))
# 10. 공백 채우기
# 공백대신 채울 문자를 : 바로 옆에다가 쓴다
# 공배대신채울문자 정렬문자 칸수
print("{0:=^10}".format('hi'))
print("{0:!<10}".format('hi'))
# 11. 소수점 표현하기











