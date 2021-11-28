class Node:
    def __init__(self, data, left_child, right_child):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


def pre_order(node):
    print(node.number, end='')
    if node.left_child != '.':
        pre_order(tree[node.left_child])
    if node.right_child != '.':
        pre_order(tree[node.right_child])


def in_order(node):
    if node.left_child != '.':
        in_order(tree[node.left_child])
    print(node.number, end='')
    if node.right_child != '.':
        in_order(tree[node.right_child])

def post_order(node):
    if node.left_child != '.':
        in_order(tree[node.left_child])
    if node.right_child != '.':
        in_order(tree[node.right_child])
    print(node.number, end='')



N = int(input())
tree = {}
for _ in range(N):
    parent, left_child, right_child = input().split()
    tree[parent] = Node(parent, left_child, right_child)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
