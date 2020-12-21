class Node:
    def __init__(self, data, left_data, right_data):
        self.parent = -1
        self.data = data
        self.left_data = left_data
        self.right_data = right_data

def in_order(node, level):
    global x, level_depth
    level_depth = max(level_depth, level)
    if node.left_data != -1:
        in_order(tree[node.left_data], level + 1)
    x_max[level] = max(x_max[level], x)
    x_min[level] = min(x_min[level], x)
    x += 1
    if node.right_data != -1:
        in_order(tree[node.right_data], level + 1)

n = int(input())
x_max = [0]
x_min = [n]
tree = {}
x = 1
level_depth = 1

for i in range(1, n + 1):
    tree[i] = Node(i, -1, 1)
    x_max.append(0)
    x_min.append(n)

for _ in range(n):
    data, left_data, right_data = map(int, input().split())
    tree[data].left_data = left_data
    tree[data].right_data = right_data
    if left_data != -1:
        tree[left_data].parent = data
    if right_data != -1:
        tree[right_data].parent = data

root = 1
for i in range(1, n + 1):
    if tree[i].parent == -1:
        root = i

in_order(tree[root], 1)

result_width = x_max[1] - x_min[1] + 1
result_level = 1
for i in range(1, level_depth + 1):
    width = x_max[i] - x_min[i] + 1
    if result_width < width:
        result_width = width
        result_level = i

print(result_level, result_width)


