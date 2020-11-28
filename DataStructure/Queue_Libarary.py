## Queue 라이브러리 사용
import queue

# 1.일반적인 큐
data_queue = queue.Queue()

# 데이터 넣기
data_queue.put("funding")
data_queue.put(1)

# 큐 사이즈 측정
print(data_queue.qsize())

# 데이터 꺼내기
print(data_queue.get())

# 큐 사이즈 측정
print(data_queue.qsize())

