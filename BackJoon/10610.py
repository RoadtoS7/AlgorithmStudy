num = str(input())  # 숫자 N을 담기위한 변수 num

numL = list()  # N이 포함하는 수를 담기 위한 리스트인 numL

for i in range(len(num)):  # 입력받은 숫자 N을 이루는 각각의 수를 리스트의 요소로서 numL에 저장한다.
    numL.append(int(num[i]))

numL.sort(reverse=True)  # numL을 인덱스 0인 숫자부터 출력했을 때 가장 큰 수 부터 출력되도록 하기 위해서 내림차순으로 정렬한다.

# 0이 가장 작은 수 이므로, 내림차순으로 정렬했을 때 리스트의 가장 끝에 위치한다. 따라서 리스트의 가장끝에 0이 있는지를 검사하여 10의 배수인지 판단한다.
# 0이 존재하지 않는다면 10의 배수가 아니므로 -1을 출력한다.
if numL[len(numL) - 1] != 0:
    print(-1)
else:

    # 10의 배수가 맞다면 각자리 수를 더하여 3의 배수인지 판단한다.
    sum = 0
    for i in range(len(numL) - 1):
        sum += numL[i]

    if sum % 3 == 0:
        # 10의 배수이면서 3의 배수인 경우라면 즉, 30의 배수라면 리스트를 인덱스 0인 자리부터 차례대로 출력한다.
        print(''.join(map(str, numL)))
    else:
        # 10의 배수이지만 3의 배수가 아닌 경우에는 -1을 출력한다.
        print(-1)