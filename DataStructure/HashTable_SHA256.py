import hashlib

hash_table = list([0 for _ in range(10)])

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16) # 16진수 문자열을 10진수 정수로 바꾸어준다.
# 해쉬 주소를 구하기 위해서 나누기 연산을 해야하기 때문에 바꾼다

def hash_function(key):
    return key % 8

def storage_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return

    else:
        hash_table[hash_address] = [index_key, value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]

    else:
        return None

print(get_key('db') % 8)
print(get_key('da') % 8)
print(get_key('dh') % 8)

storage_data('da', '010001232123')
storage_data('dh', '333333333')
print(read_data('dh'))