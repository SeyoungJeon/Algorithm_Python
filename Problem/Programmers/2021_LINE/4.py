import sys
sys.setrecursionlimit(10**6)

D, L, U, R = 0, 1, 2, 3
move_dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]


def dfs(row, col, maze, time, dir):
    if row == len(maze)-1 and col == len(maze)-1:
        return time

    if dir == R:
        new_dir = U
        left_y, left_x = row-1,col
        right_dir = D
    elif dir == D:
        new_dir = R
        left_y, left_x = row,col+1
        right_dir = L
    elif dir == L:
        new_dir = D
        left_y, left_x = row+1,col
        right_dir = U
    else:
        new_dir = L
        left_y, left_x = row,col-1
        right_dir = R

    if left_y < 0 or left_y >= len(maze) or left_x < 0 or left_x >= len(maze) or maze[left_y][left_x] == 1:
        return dfs(row, col, maze, time, right_dir)
    else:
        return dfs(left_y, left_x, maze, time+1, new_dir)


def solution(maze):
    answer = dfs(0, 0, maze, 0, R)
    return answer


print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]))