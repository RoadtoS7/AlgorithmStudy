tree = dict()

n = int(input())
for _ in range(n):
    parent, left, right = input().split(' ')
    tree[parent] = (left, right)

pre_result = ''
def pre_traversal(node):
    global pre_result
    if node == '.':
        return
    pre_result += node
    left, right = tree[node]
    pre_traversal(left)
    pre_traversal(right)

in_result = ''
def in_traversal(node):
    global in_result
    if node == '.':
        return
    left, right = tree[node]
    in_traversal(left)
    in_result += node
    in_traversal(right)

post_result = ''
def post_traversal(node):
    global post_result
    if node == '.':
        return
    left, right = tree[node]
    post_traversal(left)
    post_traversal(right)
    post_result += node

pre_traversal('A')
print(pre_result)
in_traversal('A')
print(in_result)
post_traversal('A')
print(post_result)





