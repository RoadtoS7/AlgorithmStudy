hash_table = list([0 for _ in range(10)])


def get_key(data):
    return hash(data)


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

print(hash('dk') % 8)
print(hash('da') % 8)
print(hash('dc') % 8)

storage_data('dk', '01200123123')
storage_data('da', '333333333')
print(read_data('dc'))
print(hash_table)
