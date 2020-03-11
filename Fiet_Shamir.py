import hashlib
import random

n = 997 # 출력될때 P로서 나타내어지는 소수
text = "hello" # peggy의 패스워드
g = 7 # 모두에게 공개된 g


def extended_euclidean_algorithm(a, b):
    """
    확장된 유클리드 호제법을 이용하여,
    입력된 두수의 최대공약수와
    입력된 두수인 a, b를 가지고 만들어진 다항식인 a * x + b * y == gcd를 만족하는 x, y를 반환하는 함수
    """

    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t


def inverse_of(n, p):
    """
    n 모듈라 p의 역원 값을 반환합니다.
    (n mod p == n%p )

    따라서 반환값이 m이라면 다음과 같은 식을 만족합니다.
    (n * m) % p == 1.

    유클리드 호제법의 특징상 p와 서로소인 수만  mod p 역수 값을 가집니다.
    그러나 만약 n과 p의 최대공약수 값이 1이 아니라면 n은 p와 서로소가 아니라는 뜻이며,
    n의 mod p 역원이 존재하지 않는 다는 뜻이기 때문에 에러를 발생시킵니다.

    그렇지 않는다면 n mod p 의 역원 값인 x를 반환합니다.
    """

    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        # Either n is 0, or p is not a prime number.
        raise ValueError(
            '{} has no multiplicative inverse '
            'modulo {}'.format(n, p))
    else:
        return x % p

# 크기가 1과 n(소수)사이인 랜덤 수 v
v = random.randint(1, n)

# 크기가 1과 n 사이인 랜덤 수 c
c = random.randint(1, n)

# peggy의 패스워드 출력
print("Password:\t", text)

# peggy 패스워드의 md5 해시값인 x값을 구합니다.
# 여기서는 peggy 가 이 x값을 안다는 것을 영지식 증명을 통해 벡터에게 증명하고자 합니다.
x = int(hashlib.md5(text.encode('utf-8')).hexdigest()[:8], 16) % n

# y 값을 구합니다.
# y = g의 x승의 mod n
y = pow(g, x, n)

# t값을 구합니다.
# t = g의 v승의 mod n
t = pow(g, v, n)

# r값을 구합니다.
r = (v - c * x)

# r이 0보다 작으면 mod n 의 역수를 이용하여
# r이 mod n 의 역연산을 이용하여
if r < 0:
    Result = (inverse_of(pow(g, -r, n), n) * pow(y, c, n)) % n
else:
    Result = (pow(g, r, n) * pow(y, c, n)) % n
print('======Agreed parameters============')
print('P=', n, '\t(Prime number)')
print('G=', g, '\t(Generator)')
print('======The secret==================')
print('x=', x, '\t(Peggy\'s secret)')
print('======Random values===============')
print('c=', c, '\t(Victor\'s random value)')
print('v=', v, '\t(Peggy\'s random value)')
print('======Shared value===============')
print('g^x mod P=\t', y)
print('r=\t\t', r)
print('=========Results===================')
print('t=g**v % n =\t\t', t)
print('( (g**r) * (y**c) )=\t', Result)
if t == Result:
    print('Peggy has proven she knows password')
else:
    print('Peggy has not proven she knows x')
