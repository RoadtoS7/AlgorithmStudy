## 문자열 리스트 연결하기
result = ' '.join(['apple', 'banana', 'orange'])
print(result)

## 소문자를 대문자로 바꾸기
print('apple'.upper())

## 왼쪽 공백 삭제하기
result = '    _python_    '.lstrip()
print(result)

## 왼쪽의 특정 문자 삭제하기
result = ', python.'.lstrip(',.')
print(result)

## 오른쪽 특정 문자 삭제하기
result = ', python .'.rstrip(',.')
print(result)

## 양쪽에서 특정 문자 삭제하기
result = ', pyton .'.strip(',.')
print(result)

## 문자열 왼쪽 정렬
result = 'pthon. '