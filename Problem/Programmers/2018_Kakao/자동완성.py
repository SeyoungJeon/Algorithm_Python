"""
자동완성기능
학습된 단어가 go, gone, guild 일때
- go를 찾을 때 go 모두 입력
- gone을 찾을 때 gon 입력
- guild 찾을 때 gu 입력 
총 7 글자 입력

학습된 단어들을 순서대로 찾을 때 몇 개의 문자 입력하면 되는지
프로그램 만들기

@input
단어 배열 (2<= N(배열길이) <= 100000), (2 <= L(단어 길이 총합) <= 1000000)

@output
입력해야할 총 문자 수
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

        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
            cur.count += 1

    def count(self, word):
        cur = self.head
        temp_str, count = '', 1

        for ch in word:
            temp_str += ch
            cur = cur.child[ch]
            if word == temp_str or cur.count == 1:
                break
            count += 1

        return count


def solution(words):
    answer = 0

    trie = Trie()
    for word in words:
        trie.insert(word)

    for word in words:
        answer += trie.count(word)

    return answer

"""
@ 세뚱이 풀이
1. Trie 클래스 활용
2. Node에 count 변수를 두어서 단어 몇개가 중첩되는지 표시
"""

"""
Test Case

print(solution(["go", "gone", "guild"]))
print(solution(["abc", "def", "ghi", "jklm"]))
print(solution(["word", "war", "warrior", "world"]))
"""
