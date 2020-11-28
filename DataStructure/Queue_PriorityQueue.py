import queue
data_queue = queue.PriorityQueue()

# 데이터 넣기 = 튜플(우선순위, 데이터)
data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))

# 데이터 사이즈
print(data_queue.qsize())

# 데이터 꺼내기
print(data_queue.get())
print(data_queue.get())
