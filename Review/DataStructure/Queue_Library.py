import queue

# 1. 일반적인 큐
data_queue = queue.Queue()

# 2. 데이터 넣기
data_queue.put("funding")
data_queue.put(1)

# 3. 큐 사이즈 측정
print(data_queue.qsize())

# 4. 데이터 꺼내기
print(data_queue.get())

# 5. 큐 사이즈 측정
print(data_queue.qsize())
