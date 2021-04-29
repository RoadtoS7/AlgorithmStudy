import re
from itertools import permutations
def solution(expression):

    # op =  expression내에 있는 operator 리스트
    ops = [x for x in {'+', '-', '*'} if x in expression]
    ops = [list(i) for i in permutations(ops)]
    # 숫자가 아닌 것으로 expression을 분리한다. = 연산자 기준으로 수식이 분리됨
    exp = re.split(r'(\D)', expression)

    results = []
    ## oprator 우선순위를 하나 꺼낸다.
    for op in ops:
        _exp = exp[:]
        ## 우선순위에 따라서 계산한다.
        for x in op:
            ## 연산자가 식에서 모두 계산 되어서 사라질때까지 반복해서 계산한다.
            while x in _exp:
                index = _exp.index(x)
                ## 다음번에도 eval을 사용할 것 이기 때문에 str로 감싸준다.
                _exp[index - 1] = str(eval(_exp[index - 1] + _exp[index] + _exp[index + 1]))
                # 계산완료된 부분은 없애준다.
                _exp = _exp[:index] + _exp[index + 2:]
        ## 연산자를 가지고 모두 계산했으면 결과를 넣어준다.
        results.append(_exp[0])

    ## 최댓값 계산해서 반환함.
    return max(abs(int(i)) for i in results)

print(solution("100-200*300-500+20"))