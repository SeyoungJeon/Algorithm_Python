"""
노래 가사에 사용된 단어들 중 특정 키워드가 몇 개 있는 프로그램 개발
'?'은 와일드 카드 문자
각 키워드 별로 매치되 단어가 몇개인지 순서대로 배열에 담아 반환하기

@input
가사에 사용된 모든 단어들이 담긴 배열 : words
- 2 <= 길이 <= 100000
- 1 <= 단어 길이 <= 10000 (빈 문자열인 경우 없음)
- 전체 가사 단어 길이의 합은 2 이상 1000000이하
- 중복되는 단어는 없음
- 알파벳 소문자로만 구성되어 있음

찾는 키워드가 담긴 배열 : queries
- 2 <= 길이 <= 100000
- 1 <= 키워드 길이 <= 10000 (빈 문자열 없음)
- 전체 검색 키워드 길이 합은 2이상 1000000이하
- 검색 키워드는 중복될 수 있음
- 알파벳 소문자와 와일드 카드 문자인 '?'로만 구성
- '?'이 하나 이상 포함,'?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나

@output
각 키워드 별로 매치된 단어가 몇개인지 순서대로 배열에 담아 반환
"""


class Node(object):
    def __init__(self, key):
        self.key = key
        self.child = {}
        self.count = 0


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head
        cur.count += 1

        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
            cur.count += 1

    def count(self, prefix):
        cur = self.head

        for ch in prefix:
            if ch not in cur.child:
                return 0
            cur = cur.child[ch]

        return cur.count


def solution(words, queries):
    answer = []

    front_trie = {i: Trie() for i in range(1, 10001)}
    back_trie = {i: Trie() for i in range(1, 10001)}

    for word in words:
        front_trie[len(word)].insert(word)
        back_trie[len(word)].insert(word[::-1])

    for query in queries:
        temp_query = query.replace('?', '')
        if query[0] == '?':
            answer.append(back_trie[len(query)].count(temp_query[::-1]))
        else:
            answer.append(front_trie[len(query)].count(temp_query))

    return answer

"""
@ 세뚱이 풀이
1. 순방향, 역방향 Trie 하나씩 생성
2. 단어를 삽입
3. DFS를 통해, 해당 문자열에 부합하는지 카운트 함
- 시간초과 발생

@ 다른 사람 반영한 풀이
1. 길이 (1 ~ 10000)에 따라 순방향,역방향 Trie 구조 다 만듦
2. 해당 구조에 길이에 맞게 단어 삽입
3. prefix를 replace로 구해서 count 함수에 넘겨줌
4. trie count 함수는 prefix의 마지막 원소의 count 수를 반환
"""

"""
Test Case

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["?????", "fro??", "????o", "fr???", "fro???", "pro?"]))
"""
