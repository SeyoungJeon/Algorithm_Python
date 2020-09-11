"""
기둥과 보를 이용하여 벽면 구조물을 자동으로 세우는 로봇을 개발할 계획
기둥과 보는 길이가 1인 선분으로 표현
- 규칙
    1. 기둥은 바닥위에 있거나 보의 한 쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야함
    2. 보는 한쪽 끝부분이 기둥 위에 있거나 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야함

2차원 벽면 n*n이고 각 격자는 1*1
맨 처음 벽면은 비어있는 상태
기둥과 보는 격자선 교차점에 걸치지않고
격자 칸의 각 변에 정확히 일치하도록 설치할 수 있다

@input
벽면의 크기 : n
- 5 <= n <= 100

기둥과 보를 설치하거나 삭제하는 작업이 순서대로 담긴 2차원 배열 : build_frame
- 세로 길이는 1 이상 1000 이하
- 가로 길이는 4 [x,y,a,b]
    - x,y는 기둥, 보를 설치 또는 삭제할 교차점 [가로,세로] 좌표
    - a는 설치 또는 삭제할 구조물의 종류를 나타내며 0은 기둥 1은 보
    - b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치
    - 벽면을 벗어나게 기둥, 보를 설치하는 경우 없음
    - 바닥에 보를 설치하는 경우 없음
    - 구조물은 교차점 좌표 기준으로 보는 오른쪽 기둥은 위쪽 방향으로 설치 또는 삭제
    - 구조물이 겹치도록 설치하는 경우와, 없는 구조물을 삭제하는 경우는 없음

@output
구조물의 상태
- 가로 3인 2차원 배열 [x,y,a]
    - x,y는 기둥, 보의 교차점 [가로,세로]
    - 기둥, 보는 교차점 좌표를 기준으로 오른쪽 또는 위쪽 방향 설치 되어 있음을 나타냄
    - a는 구조물의 종류 0은 기둥 1은 보
    - x좌표 기준 오름차순 정렬, x좌표 같으면 y좌표 오름차순 정렬
    - x,y좌표가 모두 같은경우 기둥이 보보다 앞에 오기
"""


def check_state(state):
    for x, y, a in state:
        if a == 0:
            if y != 0 and (x, y-1, 0) not in state and \
                    (x-1, y, 1) not in state and (x, y, 1) not in state:
                # 밑에 기둥이 없고 왼쪽에도 보가 없고 오른쪽에도 보가 없는 경우
                return False
        else:
            if (x, y-1, 0) not in state and (x+1, y-1, 0) not in state and \
                    not ((x-1, y, 1) in state and (x+1, y, 1) in state):
                # 아래에 기둥 없고 오른쪽 아래 기둥이 없고 양 옆이 보가 아닌 경우
                return False
    return True


def solution(n, build_frame):
    state = set()

    for x, y, a, b in build_frame:
        item = (x, y, a)
        if b == 1:
            state.add(item)
            if not check_state(state):
                state.remove(item)
        elif item in state:
            state.remove(item)
            if not check_state(state):
                state.add(item)

    return sorted(map(list, state), key=lambda x: (x[0], x[1], x[2]))

"""
@ 세뚱이 풀이
1. 좌표마다 위,아래,오른,왼쪽을 구성해서 보와 기둥 여부를 관리함
2. 설치물들이 하나씩 놓이거나 삭제할 때 마다 검사해서 설치하거나 삭제하려고 함
- 조건문이 너무 복잡해져서 도중에 포기하게 되었음

@ 다른 사람 풀이 반영
1. 좌표에 따른 건물을 set으로 관리
2. 해당 건물을 설치하거나 지울 경우, 먼저 건물을 설치하거나 없앤 후에 모든 건물을 검사해서 판단함
"""

"""
Test Case

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(	5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
"""
