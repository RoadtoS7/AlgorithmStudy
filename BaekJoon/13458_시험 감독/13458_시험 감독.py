## 예제 분석 결과 총감독관은 꼭 있어야 한다.

def get_judge_count(a, b, c):
    count = 1
    a -= b
    if a <= 0:
        return count


    n = a % c
    mok = a // c
    if n > 0:
        mok += 1

    return mok + count

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

res = 0
for a in A:
    count = get_judge_count(a, B, C)
    res += count

print(res)

