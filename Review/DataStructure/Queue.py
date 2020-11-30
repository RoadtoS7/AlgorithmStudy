queue = list()

def enqueue(data):
    queue.append(data)

def dequeue():
    result = queue[0]
    del queue[0]
    return result

for index in range(10):
    enqueue(index)

print(len(queue))
print(dequeue())