import hashlib

data = 'text'.encode()
hash_object = hashlib.sha1()
hash_object.update(data)
hex = hash_object.hexdigest()
print(hex)

data = 'text'.encode()
hash_object = hashlib.sha256()
hash_object.update(data)
hex = hash_object.hexdigest()
print(hex)