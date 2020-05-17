import collections

# 1. append()
deq = collections.deque(['a', 'b', 'c'])
deq.append('d')
print(deq)

# 2. appendleft(x)
deq = collections.deque(['a', 'b', 'c'])
deq.appendleft('d')
print(deq)

# 3. extend(iterable)
