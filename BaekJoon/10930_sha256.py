import hashlib

text = input()
hashvalue = hashlib.sha256(text.encode).hexdigest()
print(hashvalue)
