N = int(input())

tree = dict()
for _ in range(N):
    parent, left_child, right_child = input().split()
    tree[parent] = (left_child, right_child)


def pre_order(node):
    print(node, end='')
    if tree[node][0] != '.':
        pre_order(tree[node][0])
    if tree[node][1] != '.':
        pre_order(tree[node][1])


def order(node):
    if tree[node][0] != '.':
        order(tree[node][0])
    print(node, end='')
    if tree[node][1] != '.':
        order(tree[node][1])

def post_order(node):
    if tree[node][0] != '.':
        post_order(tree[node][0])
    if tree[node][1] != '.':
        post_order(tree[node][1])
    print(node, end='')


pre_order('A')
print()
order('A')
print()
post_order('A')