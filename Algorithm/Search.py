# 선형 탐색 알고리즘 for 정렬 안된 리스트
def linear_search(element, some_list):
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i
    return None

# 이분 탐색 알고리즘 for 정렬된 리스트
def binary_search(element, some_list):
    # 매번 범위가 바뀌고 바뀐 범위에서 중간 인덱스로 가야한다.
    # 따라서 양 끝 인덱스 값을 변수로 저장해두고 그 값을 // 2(나누기 2) 의 몫을 중간 인덱스로 정한다.
    start_index = 0
    end_index = len(some_list) - 1

    # 반복해서 중간값을 비교하여 양끝값을 바꾸므로 반복문을 돈다.
    # 원소가 하나만 남았을 경우에는 중간값이 1이 된다.
    # 만약 남아있는 값이 2 하나뿐이고 찾고자 하는 값이 1인 경우, 2의 왼쪽으로 가려고 한다.
    # 즉 0 -1 이 end값으로 대입되어 start와 end가 엇갈리는 상황이 발생할 수 있다.
    # 따라서 반복은 start <= end 까지 돌며, 두 값이 엇갈릴 때에는 값이 존재하지 않는 것이므로, None을 반환한다.
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if some_list[mid_index] == element:
            return mid_index
        elif some_list[mid_index] < element:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1

    return None
