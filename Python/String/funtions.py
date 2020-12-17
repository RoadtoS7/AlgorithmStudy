## 문자열 바꾸기 string.replace(old, new)
# 원래 문자는 바꾸지않는다. 바뀐 문자열을 반환한다.
print('Hello World'.replace('World', 'Python'))

## 문자 바꾸기
# 1. str.maketrans()를 통해 변환 테이블을 생성한다.
# 2. translate()를 호출하면 문자가 바뀐다.
table = str.maketrans('aeious', 'Python')
change_one = 'apple'.translate(table)
print(change_one)

# 문자열 분리하기
# split(구분자)

# 문자열 리스트 연결하기
# 구분자.join(문자열 리스트)
print(' '.join(['apple','banane', 'oragne']))

# 소문자를 대문자로 바꾸기
print('apple'.upper())

# 대문자를 소문자로 바꾸기
print('APPLE'.lower())

# 왼쪽 공백 삭제하기
# lstrip()
print('   python    '.lstrip())

# 오른쪽 공백 삭제하기
# rstrip()
print('   python   '.rstrip())


# 양쪽 공백 둘다 삭제하기
# strip()
print('   python   '.strip())


## 왼쪽의 특정 문자 삭제하기
# lstrip(왼쪽에서 삭제할 문자)
print(',apple.'.lstrip(',.'))

## 오른쪽의 특정 문자 삭제하기
# rstrip(오른쪽에서 삭제할 문자들)
print(',apple.'.rstrip(',.'))

## 양쪽의 특정 문자 삭제하기
print(',apple.'.strip(',.'))

## 문자열 왼쪽 정렬하기
# 인자로 주어진 수만큼 메모리를 할당한 후, 왼쪽부터 문자열을 채우고 나머지는 공백으로 채운다.
# 인자로 주어진 수보다 주어진 문자가 크다면, 공백으로 채우지 않는다.
print('python'.ljust(10))

## 문자열 오른쪽 정렬하기
# 인자로 주어진 수만큼 메모리를 할당 한 후, 오른족부터 문자열을 채우고 나머지는 공백으로 채운다.
# 인자로 주어진 수보다 주어진 문자의 길이가 크다면, 그냥 출력
print('python'.rjust(10))

## 문자열 가운데 정렬하기
# 인자로 주어진 수만큼 메모리 할당 한 후, 가운데에 문자열을 채우고, 양쪽으로 균일한 크기의 공백을 둔다.
print('python'.center(10))

## 메서드 체이닝
# 문자열 함수는 결과값으로 함수를 적용한 결과값을 반환하기 때문에, 메서드를 연속해서 호출하는 메서드 체이닝이 가능하다.
print('python'.rjust(10).upper())

## 문자열 왼쪽에 0채우기
# 인자로 주어진 수만큼 메모리를 할당한 후, 왼쪽부터 문자열을 채우고, 나머지는 0으로 채운다.
print('python'.zfill(10))

## 왼쪽부터 문자 위치 찾기
# 왼쪽부터 찾기 시작하여 첫번째로 찾은 문자의 인덱스 값을 반환한다.
# 없을 경우 -1을 반환한다.
print('python'.find('t'))
print('python'.find('i'))

## 오른쪽부터 문자 위치 찾기
# 오른쪽부터 찾기 시작하여, 첫번째로 찾은 문자의 인덱스 값을 반환한다.
# 없을 경우 -1을 반환한다.
print('python'.rfind('o'))
print('python'.rfind('i'))

## 문자열 위치 찾기 2 = index
# 왼쪽부터 찾기 시작하여, 첫번째로 찾은 문자의 인덱스 값읇 반환한다.
# 없을 경우 에러를 발생시킨다.
print('apple pineapple'.index('p'))

## 오른쪽부터 문자위치 찾기2 = rindex
print('apple pineapple'.rindex('p'))

# 문자열에 포함된 문자 개수 세기 = count
print('apple'.count('p'))
