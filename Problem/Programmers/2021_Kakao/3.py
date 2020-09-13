from collections import deque
import bisect


class Node(object):
    def __init__(self, key):
        self.key = key
        self.child = {}
        self.score_list = []


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, key_word):
        cur = self.head
        for idx in range(len(key_word)-1):
            if key_word[idx] not in cur.child:
                cur.child[key_word[idx]] = Node(key_word[idx])
            cur = cur.child[key_word[idx]]
        cur.score_list.append(int(key_word[-1]))

    def search(self, key_word):
        cur = self.head

        cur_list = deque([cur])

        for idx in range(len(key_word)-1):
            basic_len = len(cur_list)
            key = key_word[idx]

            temp = 0
            while temp < basic_len:
                pos = cur_list.popleft()
                if key == '-':
                    for child in pos.child:
                        cur_list.append(pos.child[child])
                else:
                    if key in pos.child:
                        cur_list.append(pos.child[key])

                temp += 1

        count = 0
        for cur in cur_list:
            cur.score_list.sort()
            value = bisect.bisect_left(cur.score_list, int(key_word[-1]))
            count += 0 if len(cur.score_list) == value else len(cur.score_list) - value

        return count


def solution(info, query):
    answer = []

    trie = Trie()
    score_list = []

    for value in info:
        value = value.split(' ')
        score_list.append(int(value[-1]))
        trie.insert(value)

    score_list.sort()

    for value in query:
        value = value.split('and')
        for idx in range(len(value)):
            if idx < len(value)-1:
                value[idx] = value[idx].strip()
            else:
                value.extend(value[idx].strip().split(' '))
                value.remove(value[idx])

        if value[0] == '-' and value[1] == '-' and value[2] == '-' and value[3] == '-':
            temp = bisect.bisect_left(score_list, int(value[-1]))
            answer.append(0 if len(score_list) == temp else len(score_list) - temp)
        else:
            answer.append(trie.search(value))

    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))