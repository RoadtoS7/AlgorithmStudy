# cmp_to_key는 매개변수 key로 주어진 함수가 1을 반환하면
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    print('t1=', t1, 't2=', t2)
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer


solution([6, 10, 2])