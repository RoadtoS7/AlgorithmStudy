## 해쉬 테이블 만들기
hash_table = list([0 for i in range(10)])
print(hash_table)

# 키 생성 함수
# 데이터에 따라서 키생성하는 방법을 정의해줘야한다.
# ord()사용 = 입력의 아스키 코드 값을 반환
def get_key(data):
    return ord(data[0])

# 해쉬 함수
# 가장 간단한 방식 사용 = division 기법
# = 나누기의 나머지 값을 해쉬값으로 사용하는 기법
def hash_function(key):
    return key % 5

def storage_data(data, value):
    key = get_key(data)
    hash_address = hash_function(key)
    hash_table[hash_address] = value

def read_data(data):
    key = get_key(data)
    hash_address = hash_function(key)
    return hash_table[hash_address]

storage_data('Andy', '0105553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '0102222333')
print(read_data('Dave'))
