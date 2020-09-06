"""
동적으로 게임 시간을 늘려서 난이도 조절하기로 했다
실패율은 다음과 같이 정의한다
- 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

@input
전체 스테이지의 개수 : N (1 <= N <= 500)
현재 멈춰있는 스테이지의 번호가 담긴 배열 : stages
- 1<= len(stages) <= 200000
- 1 <= stage <= N+1 이하의 자연수
   - 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다
   - 단, N+1은 N 번째 스테이지까지 클리어한 사용자를 나타낸다

@output
실패율이 높은 스테이부터 내림차순으로 스테이지 번호가 담긴 배열
- 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하기
- 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의
"""
from collections import Counter


def solution(N, stages):
    user_len, fail_list, count, stages = len(stages), [], 0, Counter(stages)
    for stage in range(1, N+1):
        fail = stages[stage] / (user_len - count) if user_len - count > 0 else 0
        fail_list.append((fail, stage))
        count += stages[stage]

    return [value[1] for value in sorted(fail_list, key=lambda x: (-x[0], x[1]))]


"""
@세뚱이 풀이
1. Counter를 이용해서 해당 stage 마다 개수를 세기
2. 해당 실패율을 계산해서 튜플형식의 리스트로 관리
3. 실패율에 따른 내림차순, 스테이지에 따른 오름차순 정렬

@ 이전 풀이에서 변경한 점
1. 변수의 선언을 한 줄로 변경
2. while문에서 for 문으로 변경
3. answer 변수에 넣어서 반환하지 않고 바로 정답을 반환
"""

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4, 4, 4, 4, 4]))