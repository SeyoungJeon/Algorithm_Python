"""
잠겨있는 자물쇠 N*N 크기 정사각형 격자 형태
특이한 모양 열쇠는 M*M 크기인 정사각 격자 형태
자물쇠에는 홈이, 열쇠에는 홈과 돌기 (회전과 이동 가능)
열쇠의 돌기 부분을 자물쇠 홈 부분에 딱 맞게 채우면 잘무쇠가 열리는 구조
자물쇠 영역 외에서는 열쇠의 홈과 돌기가 영향을 주지 않음
열쇠의 돌기와 자물쇠의 돌기는 만나서 안됨
자물쇠의 모든 홈을 채워야 함

@input
열쇠 2차원 배열 : key
- M*M (3 <= M <= 20)
자물쇠 2차원 배열 : lock
- N*N (3 <= N <= 20)

M은 항상 N 이하
key와 lock의 원소는 0 (홈), 1 (돌기) 로만 구성

@output
자물쇠 풀 수 있는지 boolean 형식 반환
"""
import copy


def rotate_90(m):
    N = len(m)
    ret_90, ret_180, ret_270 = [[0] * N for _ in range(N)], [[0] * N for _ in range(N)], [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret_90[c][N - 1 - r] = m[r][c]              # 90도 회전
            ret_180[N - 1 - r][N - 1 - c] = m[r][c]     # 180도 회전
            ret_270[N - 1 - c][r] = m[r][c]             # 270도 회전

    return ret_90, ret_180, ret_270


def solution(key, lock):
    key_list = [key, (*rotate_90(key))]

    lock_len, key_len = len(lock), len(key)-1
    for idx in range(0, key_len):
        lock.insert(0, [-1] * lock_len)
        lock.append([-1] * lock_len)

    for idx in range(len(lock)):
        for i in range(key_len):
            lock[idx].insert(0, -1)
            lock[idx].append(-1)

    for value in key_list:
        for r in range(lock_len + key_len):
            for c in range(lock_len + key_len):
                temp = copy.deepcopy(lock)

                for key_r in range(len(key)):
                    for key_c in range(len(key)):
                        if temp[r+key_r][c+key_c] < 0:
                            continue

                        temp[r+key_r][c+key_c] += value[key_r][key_c]

                flag = True
                for i in range(key_len, key_len + lock_len):
                    for j in range(key_len, key_len + lock_len):
                        if temp[i][j] != 1:
                            flag = False
                            break
                    if not flag:
                        break

                if flag:
                    return True

    return False

"""
@ 세뚱이 1차 시도
1. 0, 90, 180, 270 회전된 key 리스틀 구한다.
2. 각 키에 대해 DFS를 통해 키가 될 수 있는 모든 경우를 구한다.
3. 모든 경우에 대해 자물쇠에 맞는지 검사한다.
- 대부분 시간 초과, 2~3개 런타임 에러 

@ 세뚱이 2차 시도 
1. 0, 90, 180, 270 회전된 key 리스틀 구한다.
2. zero padding을 통해, lock 배열을 늘린다.
3. 늘려진 lock 배열에서 key를 움직여서 맞는지 찾는다.
- 시간이 꽤 많이 걸려서 점수를 많이 얻진 못했다.
"""




print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))