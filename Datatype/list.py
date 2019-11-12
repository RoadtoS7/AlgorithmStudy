a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])

# 'a'값을 인덱싱으로 꺼내는 방법
print(a[3][0])
print(a[-1][1])
print(a[-1][2])

# 2. 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0: 2])
# [1, 2]

b = a[:2]
c = a[2:]
print(b)
print(c)

# 중첩된 리스트에서 슬라이싱하기 = 똑같은 방법
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

#3. 리스트 연산하기
# + : 리스트를 이어붙인다.
a = [1, 2, 3 ]
b = [4, 5, 6]
print(a+b)

# * : 리스트를 반복하여 새로운 리스트를 만든다.
print(a * 3)

#4. 리스트 길이 구하기 = len()
a = [1, 2, 3]
print(len(a))
# len함수는 튜플과 딕셔너리에서도 사용할 수 있다.

# 리스트 연산 오류
a = [1, 2, 3 ]
print(str(a[2]) + 'hi')
# 자료형이 다른 것 끼리는 더하기 연산을 할 수 없다.

# 5. 리스트의 수정과 삭제
# 1) 수정
# 리스트는 문자열과 달리 인덱싱을 사용하여 수정할 수 있다.
a = [1, 2, 3]
a[2] = 4
print(a)

# 2) 삭제 = del 함수 사용하기
# del a[x] 는 a 리스트에서 x번째 요소값을 삭제한다.
# del 객체(파이썬에서 사용되는 모든 자료형)
a = [1, 2, 3]
del a[1]
print(a)

# del 이용 여러 요소 한번에 삭제 가능
a = [1, 2, 3, 4, 5]
del a[2:]
print(a)
# 3) 삭제 = remove(), pop() 이용

# 6. 리스트 관련 함수들
# 리스트뒤에 . 을 붙여서 여러 함수를 사용할 수 있다.
# 1) 리스트에 요소x 추가 = append(x)
a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])
print(a)

# 2) 리스트 정렬 = sort()
a = [1, 4, 3, 2]
a.sort()
print(a)
# 문자도 알파벳 형식으로 정렬할 수 있다.
a = ['a', 'c', 'b']
a.sort()
print(a)

#3) 리스트 역순으로 뒤집기 = reverse()
a = ['a', 'c', 'b']
a.reverse()
print(a)

# 4) 리스트에 x값이 있으면 x의 위치값(인덱스 값)을 반환 = index()
# 존재하지 않는 값을 찾고자 할 경우 오류 발생
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))
# print(a.index(0))

# 5) 리스트의 a번째 위치(인덱스)에 b 삽입 = insert(a,b)
a = [1, 2, 3]
a.insert(0, 4)
print(a)

a.insert(3, 5)
print(a)

# 6) 리스트에서 첫번째로 나오는 x 요소 삭제 = remove(x)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
a.remove(3)
print(a)

# 7) 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제된다. = pop()
a = [1, 2, 3]
b= a.pop()
print(b)
print(a)
# 8) 리스트에서 x 번째 위치의 요소를 돌려주고 그 요소는 삭제된다. = pop(x0
a = [1, 2, 3]
b= a.pop(1)
print(b)
print(a)

# 9) 리스트에 포함된 요소 x의 개수세기 = count(x)
a = [1, 2, 3, 1]
print(a.count(1))

# 10) 입력인자로 리스트만 올 수 있음 + 원래 리스트에 입력인자 리스트를 더한다. = extend()
a = [1, 2, 3]
a.extend([4, 5])
print(a)

b = [6, 7]
a.extend(b)
print(a)








