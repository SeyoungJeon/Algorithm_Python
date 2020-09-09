"""
블록게임 프로그램 만들기
N*N 크기 보드 위에 블록들이 배치된 채로 게임이 시작
플레이어는 위쪽에서 1*1 크키의 검은 블록을 떨어뜨려 쌓을 수 있다
이 때, 검은블록과 기존에 놓인 블록을 합해 속이 꽉 채워진 직사각형을 만들 수 있다면
그 블록을 없앨 수 있다

검은 블록을 떨어뜨려 없앨 수 있는 블록 개수의 최댓값 구하기

@input
블록의 상태가 들어있는 N*N 의 2차원 배열 : board
- 1 <= N <= 50
- 0 <= 원소 <= 200
- 0은 빈칸 
- 각 블록은 숫자를 이용해 표현
- 서로 다른 블록은 서로 다른 숫자로 표현

@output
없앨 수 있는 최대 블록 개수
"""


def solution(board):
    answer = 0

    block_dict = {}
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if board[row][col] > 0:
                if board[row][col] not in block_dict:
                    block_dict[board[row][col]] = [(row, col)]
                else:
                    block_dict[board[row][col]].append((row, col))

    temp_block_dict = {}
    for key in block_dict:
        value = list(map(list, zip(*block_dict[key])))
        min_y, max_y = min(value[0]), max(value[0])
        min_x, max_x = min(value[1]), max(value[1])

        temp_block_dict[key] = []
        for row in range(min_y, max_y+1):
            for col in range(min_x, max_x+1):
                if (row, col) not in block_dict[key]:
                    temp_block_dict[key].append((row, col))

    while True:
        break_block = []
        for key in temp_block_dict:
            value1, value2 = temp_block_dict[key][0], temp_block_dict[key][1]
            value1_y, value1_x = value1
            wall_value1, wall_value2 = True, True
            while value1_y >= 0:
                if board[value1_y][value1_x] > 0:
                    wall_value1 = False
                    break
                value1_y -= 1

            value2_y, value2_x = value2
            while value2_y >= 0:
                if board[value2_y][value2_x] > 0:
                    wall_value2 = False
                    break
                value2_y -= 1

            if wall_value1 and wall_value2:
                break_block.append(key)

        for block in break_block:
            answer += 1
            for pos in block_dict[block]:
                board[pos[0]][pos[1]] = 0
            block_dict.pop(block)
            temp_block_dict.pop(block)

        if len(break_block) == 0:
            break

    return answer

"""
@ 세뚱이 풀이
1. 현재 블럭에 대한 모든 y,x 좌표를 dictionary로 관리
2. 직사각형을 만들기 위해 채워야할 y,x 좌표를 dictionary로 관리
3. 채워야할 좌표들을 위에서 떨어뜨렸을 때, 채울 수 있는지 확인
4. 해당 좌표들을 모두 채운다면, 관리하는 dictionary에서 지우고 board에서도 해당 좌표 0으로 처리
5. 총 없어지는 블럭 개수 세기

@ 다른 사람 풀이 반영할 점
1. numpy 라이브러리를 사용하는 사람이 많은데, 추후에 해당 라이브러리 공부를 좀 해야겠다.

"""

"""
Test Case

print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))
"""
