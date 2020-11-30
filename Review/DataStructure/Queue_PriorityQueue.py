import queue

data_list = queue.PriorityQueue()

# 데이터 넣기 = 튜플(우선순위, 데이터)
data_list.put((10, "korea"))
data_list.put((5, 1))
data_list.put((15, "china"))

# 데이터 사이즈
print(data_list.qsize())

# 데이터 꺼내기
print(data_list.get())
print(data_list.get())