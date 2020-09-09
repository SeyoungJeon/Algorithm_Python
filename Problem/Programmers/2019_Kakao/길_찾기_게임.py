"""
라리언은 게임을 구상했다.
카카오 프렌즈를 두 팀으로 나누고, 각 팀이 같은 곳을
다른 순서로 방문하도록 해서 먼저 순회를 마친 팀이 승리
라이언은 방문할 곳의 2차원 좌표값을 구하고
각 장소를 이진트리의 노드가 되도록 구성한 후, 순회 방법을 힌트로 주어
각 팀이 스스로 경로를 찾도록 한다.
특별한 규칙으로 트리 노드를 구성
1. 트리를 구성하는 모든 노드의 x,y 좌표 값은 정수
2. 모든 노드는 서로 다른 x 값을 가짐
3. 같은 Level에 있는 노드는 같은 y좌 표를 가진다
4. 자식 노드의 y 값은 항상 부모 노드보다 작음
5. 임의의 노드 V의 왼쪽 서브트리에 있는 모든 노드의 x 값은 V의 x값보다 작다
6. 임의의 노드 V의 오른쪽 서브 트리에 있는 모든 노드의 x 값은 V의 x값보다 크다
전위 순회와 후위순회 구하기

@input
이진트리를 구성하느 노드들의 좌표 배열 : nodeinfo
- 1 <= 길이 <= 10000
- 0 <= 좌표값 <= 100000
- 트리의 깊이 100 이하인 경우만 입력으로 주어진다
- 잘못된 노드 위치가 주어지는 경우는 없다

@output
전위 순회, 후위 순회 결과를 2차원 배열에 담아 반환
"""
import sys
sys.setrecursionlimit(10**6)


class Node(object):
    def __init__(self, x, num):
        self.pos_x, self.num = x, num
        self.left = self.right = None


class BinaryTree(object):
    def __init__(self):
        self.head = None

    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while True:
                if cur.pos_x < node.pos_x:
                    if cur.right is None:
                        cur.right = node
                        break
                    else:
                        cur = cur.right
                else:
                    if cur.left is None:
                        cur.left = node
                        break
                    else:
                        cur = cur.left

    def preorder_traversal(self, node):
        traversal = [node.num]
        if node.left is not None:
            traversal += self.preorder_traversal(node.left)
        if node.right is not None:
            traversal += self.preorder_traversal(node.right)
        return traversal

    def postorder_traversal(self, node):
        traversal = []
        if node.left is not None:
            traversal += self.postorder_traversal(node.left)
        if node.right is not None:
            traversal += self.postorder_traversal(node.right)
        traversal.append(node.num)
        return traversal


def solution(nodeinfo):
    nodeinfo = sorted([(nodeinfo[idx][0], nodeinfo[idx][1], idx + 1) for idx in range(0, len(nodeinfo))],
                      key=lambda x: -x[1])
    bin_tree = BinaryTree()

    for node in nodeinfo:
        bin_tree.insert(Node(node[0], node[2]))

    return [bin_tree.preorder_traversal(bin_tree.head), bin_tree.postorder_traversal(bin_tree.head)]


"""
@ 세뚱이 풀이
1. y좌표를 기준으로 내림차순 정렬
2. 이진트리 생성
3. [전위 순회, 후위순회] 반환
** 재귀함수가 있는 경우. 최대 재귀 깊이 설정 sys.setrecursionlimit(10**6) 
"""

"""
Test Case

print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
"""
