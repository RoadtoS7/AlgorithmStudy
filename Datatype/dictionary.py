# Key 리스트 만들기
a = {'name' : 'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.keys())

for k in a.keys():
    print(k)

print(list(a.keys()))

# Value 리스트 만들기
print(a.values())

#3) key, value 쌍 만들기 = items()
print(a.items())

# 4) key:value 쌍 모두 지우기 : clear()
# print(a.clear())
# {}

# 5) key로 value 얻기 = get(key) = dict[key]
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.get('name'))
# 'pey'
a.get('phone')
# '0119993323'

# 존재하지 않는 키에 대응되는 value를 가져오라고 할 경우 None 반환
# <> a[존재하지 않는 키] : key에러 발생
print(a.get('nokey'))
# None
# print(a['nokey'])
# nokey 에러 발생

#key값일 없을 경우 지정된 default값을 가져오도록 하고 싶은 경우 = get(x, '디폴트 값')
print(a.get('foo', 'bar'))
# 'bar'

# 6) 해당 키가 딕셔너리 안에 있는지 조사하기 = in(key)
print('name' in a)
# True
print('email' in a)
# False

