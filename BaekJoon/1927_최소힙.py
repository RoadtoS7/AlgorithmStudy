class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1
        if left_child_popped_idx >= len(self.heap_array):  # 왼쪽 자식 노드가 없을 때: 자식 노드가 존재하지 않음을 의미
            return False
        elif right_child_popped_idx >= len(self.heap_array):  # 왼쪽 자식 노드는 있고, 오른쪽 자식 노드 없을 때
            if self.heap_array[popped_idx] > self.heap_array[
                left_child_popped_idx]:  # 새로운 루트 노드의 값 < 왼쪽 자식 노드: 움직일 수 있음
                return True
            else:
                return False  # 움직일 수 없음 = 현재 위치가 맞음
        else:  # 왼쪽 자식, 오른쪽 자식 둘다 있는 경우
            if self.heap_array[left_child_popped_idx] < self.heap_array[right_child_popped_idx]:
                if self.heap_array[left_child_popped_idx] < self.heap_array[popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx] > self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1:
            return 0
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # 오른쪽 자식 노드가 없을 때
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] > self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[
                                                                                              left_child_popped_idx], \
                                                                                          self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
            else:  # 오른쪽, 왼쪽 자식 노드 둘다 있는 경우
                if self.heap_array[left_child_popped_idx] < self.heap_array[right_child_popped_idx]:
                    if self.heap_array[left_child_popped_idx] < self.heap_array[popped_idx]:
                        self.heap_array[left_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[
                                                                                                  popped_idx], \
                                                                                              self.heap_array[
                                                                                                  left_child_popped_idx]
                        popped_idx = left_child_popped_idx
                else:
                    if self.heap_array[right_child_popped_idx] < self.heap_array[popped_idx]:
                        self.heap_array[right_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[
                                                                                                   popped_idx], \
                                                                                               self.heap_array[
                                                                                                   right_child_popped_idx]
                        popped_idx = right_child_popped_idx
        return returned_data

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] < self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[parent_idx], self.heap_array[inserted_idx] = self.heap_array[inserted_idx], self.heap_array[parent_idx]
            inserted_idx = parent_idx
        return True

n = int(input())
heap = Heap(0)
heap.pop()
for _ in range(n):
    data = int(input())
    if data == 0:
        print(heap.pop())
    else:
        heap.insert(data)