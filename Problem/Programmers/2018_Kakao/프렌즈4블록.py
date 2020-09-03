"""
블록 2*2 형태로 붙어 있을 경우 사라지며 점수 얻는 게임
겹쳐 있어도 사라짐, 2*2 모양이 여러개 있다면 한꺼번에 사라짐
지워진 후에 위에 있는 블럭들은 아래로 떨어짐
지워지는 블록 몇개 인지 구하라

@input
판의 높이 : m (2 <= n <= 30)
판의 폭 : n  (2 <= n <= 30)
배치 정보 : board (element : A ~ Z)

@output
지워지는 불록 개수
"""


def solution(m, n, board):
    answer = 0
    stack = list(map(list, board))

    while True:
        pos_set = set()
        
        # 사라져야할 블록 위치 찾기
        for i in range(m-1):
            for j in range(n-1):
                if '0' != stack[i][j] == stack[i+1][j] == stack[i][j+1] == stack[i+1][j+1]:
                    pos_set |= set([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])
  
        # 사라져야할 블록이 없다면
        if len(pos_set) == 0:
            break

        # 사라져야할 블록 개수 추가 및 '0'으로 표시
        answer += len(pos_set)
        for i, j in pos_set:
            stack[i][j] = '0'
        
        # 사라진 블록보다 위에 존재하는 블록 떨어뜨리기
        for i in range(m-2, -1, -1):
            for j in range(n):
                if stack[i][j] != '0':
                    cur_y = i
                    while cur_y + 1 < m and stack[cur_y + 1][j] == '0':
                        cur_y += 1
                    
                    # 이전 위치의 값과 떨어진 지점의 값 교환
                    stack[cur_y][j], stack[i][j] = stack[i][j], stack[cur_y][j]

    return answer

"""
@ 세뚱이 풀이
1. board 원소들을 2차원 배열로 변환
2. 이중 반복문을 통해, 사라질 블럭들의 위치를 집합 set에서 관리
3. set에 있는 pos들을 '0' 으로 변경
4. 이중 반복문을 통해, 사라진 블럭들을 채움

@ 다른 사람 풀이 중 참고해서 반영할 점
1. if 조건문 간단하게 작성 (== 을 통해 다 비교 가능)
2. |= 을 통해, 합집합 계산을 간단하게 할 수 있음
3. 원소가 튜플일 경우에는 for i,j 로 나타낼 수 있음
4. swap 할 경우, 변수1, 변수2 = 변수2, 변수1 이용
"""

"""
Test Case
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(	6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
"""
