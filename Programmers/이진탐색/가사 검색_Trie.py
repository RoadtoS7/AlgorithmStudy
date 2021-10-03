from sys import stdin
from collections import defaultdict
input = stdin.readline

# Trie의 구성요소, 문자 하나를 담는다.
class Node:
    def __init__(self, key):
        self.key = key # key가 문자에 해당한다.
        self.child = {}
        self.length = defaultdict(int) # length값을 저장하는 default dict

# Trie
class Trie:
    def __init__(self):
        self.head = Node(None)

    # Trie에 문자열을 추가한다.
    def insert(self, word):
        cur = self.head
        cur.length[len(word)] += 1

        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur.child[ch].length[len(word)] += 1
            cur = cur.child[ch]
        cur.child['*'] = True

    # Trie에서 문자열이 존재하는지 찾는다.
    def search(self, prefix, length):
        cur = self.head
        for ch in prefix:
            if ch not in cur.child:
                return 0
            else:
                cur = cur.child[ch]

        return cur.length[length]


def solution(words, queries):
    answer = []
    trie = Trie()
    r_trie = Trie()

    for word in words:
        trie.insert(word)
        r_trie.insert(word[::-1])

    for query in queries:
        if word == "?"*len(word):
            answer.append(trie.head.length[len(word)])
        if query[0] != '?':
            prefix = query.split("?")[0]
            answer.append(trie.search(prefix, len(query)))
        else:
            prefix = query[::-1].split("?")[0]
            answer.append(r_trie.search(prefix, len(query)))

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))





