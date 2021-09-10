# 점수: 1점

def solution(n, arr1, arr2):
    secret1, secret2 = [], []

    for i in range(n):
        bin1, bin2 = bin(arr1[i]), bin(arr2[i])
        str1, str2  = str(bin1)[2:], str(bin2)[2:]
        len_str1, len_str2 = len(str1), len(str2)
        for i in range(n - len_str1):
            str1 = '0' + str1
        for j in range(n - len_str2):
            str2 = '0' + str2


        secret1.append(str1)
        secret2.append(str2)

    answer = []

    for i in range(n):
        temp = []
        for j in range(n):
            if secret1[i][j] == '0' and secret2[i][j] == '0':
                temp.append(" ")
            else:
                temp.append("#")
        answer.append("".join(temp))

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))