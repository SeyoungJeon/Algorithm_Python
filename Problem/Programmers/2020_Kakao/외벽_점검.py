"""
주기적으로 외벽의 상태를 점검
외벽의 총 둘레는 n미터, 손상될 수도 있는 취약한 지점이 있음
점검시간은 1시간으로 제한
최소한의 친구들을 투입해 취약 지점을 점검하고 
나머지 친구들은 내부 공사를 돕는다
정북 방향 지점 0
취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리
친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동

@input
외벽의 길이 : n ( 1<= n <= 200)
취약 지점의 위치가 담긴 배열 : weak
- 1<= 길이 <= 15
- 두 취약점의 위치가 같은 경우는 없음
- 취약 지점의 위치는 오름차순 정렬로 주어짐
- weak 원소는 0 이상 n-1 이하 정수

각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 : dist
- 1 <= 원소 <= 100

@output
취약 지점을 점검하기 위해 보내야 하는 친구 수의 최솟값
- 친구들 모두 투입해도 취약 지점 전부 점검할 수 없는 경우 -1
"""
from itertools import permutations


def solution(n, weak, dist):
    L = len(weak)
    cand = []
    weak_point = weak + [w+n for w in weak]  # 선형으로

    for i, start in enumerate(weak):
        for friends in permutations(dist):  # 순열 이용
            count = 1
            position = start

            for friend in friends:
                position += friend

                if position < weak_point[i+L-1]:
                    count += 1

                    position = [w for w in weak_point[i+1:i+L] if w > position][0]
                else:  # 끝 포인트까지 도달
                    cand.append(count)
                    break

    return min(cand) if cand else -1

"""
@ 세뚱이 풀이
- 이 문제 접근 방법조차 떠올릴 수 없었다.

@ 다른 사람 풀이 참고
1. weak를 선형형태로 변경하기 weak + [w+n for w in weak]
2. permutation으로 사람들을 취약지점에 배치 시켜서 투입 인원수 모든 경우 찾기
3. 최소 투입 인원수로 반환
"""

"""
Test Case

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
"""

