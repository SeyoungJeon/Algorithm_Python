## Trie

- prefix tree라고도 불림
- 문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태 자료구조
- 빠르게 탐색이 가능하다는 장점이 있으나, 저장 공간의 크기가 크다는 단점이 있음
- 검색어 자동완성, 사전에서 찾기, 문자열 검사에 주로 사용



#### 시간 복잡도

- 제일 긴 문자열의 길이 : L , 총 문자열들의 수 : M
  - 생성 시간복잡도 O(M*L) [삽입 자체는 O(L)]
  - 탐색 시간복잡도 O(L)



#### Python Code

```python
# 저장 공간 노드
class Node(object):
    def __init__(self, key):
        self.key = key
        self.child = {}

# Trie class
class Trie(object):
    def __init__(self):		# 첫 생성시 빈 Node를 head로 가짐
        self.head = Node(None)
    
    def insert(self, word):
        cur = self.head
        
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.child['*'] = True		# '문자열 끝을 표시'
    
    def search(self, word):
        cur = self.head
        
        for ch in word:
			if ch not in cur.child:
                return False
           	cur = cur.child[ch]
        
        if '*' in cur.child:
            return True
```





