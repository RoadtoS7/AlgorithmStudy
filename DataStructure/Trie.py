# Trie의 구성요소, 문자 하나를 담는다.
class Node:
    def __init__(self, key):
        self.key = key # key가 문자에 해당한다.
        self.child = {}

# Trie
class Trie:
    def __init__(self):
        self.head = Node(None)

    # Trie에 문자열을 추가한다.
    def insert(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]

        cur.child['*'] = True

    # Trie에서 문자열이 존재하는지 찾는다.
    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]

        return '*' in cur.child


# test code
trie = Trie()
trie.insert('kim')
trie.insert('suhyeon')
trie.insert('naver')
trie.insert('kakao')
trie.insert('line')
trie.insert('gan')
trie.insert('da')

print(trie.search('suhyeon'))
print(trie.search('naver'))
print(trie.search('naverkakao'))
print(trie.search('kakao'))
print(trie.search('line'))

