## 해쉬 테이블 만들기
hash_table = list([i for i in range(10)])
print(hash_table)

## 해쉬 함수
# 가장 간단한 방식 사용 = division 기법
# = 나누기의 나머지값을 해시값으로 사용하는 기법
def hash_func(key):
    return key % 5

## 해쉬 테이블에 데이터 저장하기
# 데이터에 따라서 키생성 방법 정의 필요
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'
# 키생성방법 = 데이터의 첫번째 문자의 아스키 코드값
# 아스키 코드 반환하는 함수 = ord()
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(ord(data1[0]), hash_func(ord(data1[0])))
print(ord(data1[0]), ord(data4[0]))

# 데이터 저장 함수
def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

# 데이터 가져오는 함수
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

storage_data('Andy', '0105553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '0102222333')
print(get_data('Andy'))