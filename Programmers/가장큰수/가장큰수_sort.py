## 문자열의 인덱스 0부터 비교하는 특성을 이용한 것이다!

## 첫번째 풀이
# 숫자가 1000이하라는 것을 이용하여 numbers.sort(key=lambda x:x+3, reverse=True)를 해서 정렬한다.
# ['666', '101010', '222']를 정렬하면 ['666', '222', '101010'] 이 되어서 결과적으로 6210이 된다.
# 이렇게 되는 이유: 문자열 비교연산의 경우 첫번째 인덱스 끼리 아스키 코드로 바꿔서 비교후 동일하면 두번째 인덱스의 아스키 코드로 비교한다.
# 따라서 6, 2, 1의 아스키 코드끼리 비교하므로 6210이 결과로 나오는 것이다.


# 람다: sort()와 sorted() 함수 모두 비교전에 호출할 함수를 지정하는 key 매개변수를 가지고 있다.
# 따라서 아래에서는 비교 전에 x * 3을 실행하여, ['666', '101010', '222']가 되며, 이 상태로 정렬을 수행한다.
def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(str_numbers))) # ['0', '0', '0', '0']을 join하면 '0000'이 되기 때문에 이를 방지 하기 위해서 int를 한 후 다시 str해준다.


