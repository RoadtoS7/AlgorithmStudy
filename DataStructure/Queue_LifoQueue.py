import queue
data_queue = queue.LifoQueue()

data_queue.put("funding")
data_queue.put(1)
print(data_queue.qsize())
print(data_queue.get())

