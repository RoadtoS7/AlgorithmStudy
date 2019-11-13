# 1. 집합 자료형 만드는 방법
s1 = set([1, 2, 3])
print(s1)
s2 = set('Hello')
print(s2)

# 2. 집합 자료형 특징
# 1) 중복을 허용하지 않는다.
# 2) 순서가 없다. -> 인덱싱을 사용할 수 없다.
# 3) 인덱싱 사용to 리스트, 투플 자료형으로 형변환 must
s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)
# [1, 2, 3]

print(l1[0])
# 1

t1 = tuple(s1)
print(t1)
# (1, 2, 3)

print(t1[0])
# 1

# 3. 교집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
# 1) 교집합
print(s1&s2)
# {4, 5, 6}
print(s1.intersection(s2))
# {4, 5, 6}

# 2) 합집합
print(s1|s2)
# {1, 2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))
# {1, 2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 9}

# 3) 차집합 구하기
print(s1-s2)
# {1, 2, 3}
print(s2-s1)
# {8, 9, 7}
print(s1.difference(s2))
# {1, 2, 3}
print(s2.difference(s1))
# {8, 9, 7}

# 4. 집합 관련 함수들

