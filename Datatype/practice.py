# 1
print((80+75+55)/ 3)

# 3
a = "881120-1068234"
print(a[:6])
print(a[6:])

# 4.
print(a[7])

# 5
a = "a:b:c:d"
b = a.replace(':', '#')
print(a)

# 6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 7
b=''
a = ['Life', 'is', 'too', 'short']

print(' '.join(a))

# 8
a = (1, 2, 3)
print(a + (4,))
# a 값이 변경되는 것이 아니다. b) 튜플은 그 값을 변경할 수 없다.
# 새로운 튜플이 생성되고 그 값이 변수 a에 들어가는 것이다.
# 주소값 변경여부 확인 = id(a)

# 9
# (3): key값으로 리스트 들어올 수 없다. = 변하는 값 들어올 수 없다.

# 10
a = {'A': 90, 'B': 80, 'C': 70}
print(a.pop('B'))
print(a)

# 11
s = set(a)
print(list(s))

# 12
# b에서 인덱스 1위치에 잇는 값도 4로 변하게 된다.
# b) a = b 이렇게 복사하면, a변수와 b변수는 같은 리스트 객체를 가리키고 있기 때문이다.




