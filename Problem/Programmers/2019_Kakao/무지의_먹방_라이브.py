"""
무지는 먹방을 한다.
N 개의 음식이 있다 ( 1~ N 까지 번호가 붙어 있는데, 각 음식을 먹는데 일정 시간소요 된다)
1. 1번부터 음식 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다
2. 마지막 번호 음식을 섭취한 후에는 다시 1번 음식이 무지 앞으로 온다
3. 음식 하나를 1초 동안 먹고 그대로 두고 다음 음식 섭취
    - 다음 음식은 남은 음식 중 다음으로 섭취해야 할 가장 가까운 음식을 말함
4. 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다

무지가 먹방을 시작한지 K 초후에 방송이 잠시 중단
방송을 다시 이어갈 때 몇번 음식을 섭취해야하는 지알고자 한다

@input
각 음식을 모두 먹는데 필요한 시간이 담겨 있는 배열 : food_times
- 음식의 번호 순서대로 시간이 담겨 있다
- 1 <= 길이 <= 2000
- 1 <= 원소 <= 1000
** 효율성
- 1 <= 길이 <= 2000000
- 1 <= 원소 <= 100000000

네트워크 장애 발생한 시간 ; K
- 1 <= k <= 2000000
** 효율성
- 1 <= k <= 2*10^13

@output
몇 번음식부터 다시 섭취하면 되는지 음식 번호
만약 섭취할 음식 없으면 -1 반환
"""
from collections import deque


def solution(food_times, k):
    food_times = deque(sorted([(food_times[idx], idx+1) for idx in range(0, len(food_times))]))
    prev, time = 0, 0
    while len(food_times) > 0:
        value = food_times.popleft()
        if (value[0] - prev) * (len(food_times) + 1) + time > k:
            food_times.appendleft(value)
            break

        time += (value[0] - prev) * (len(food_times) + 1)
        prev = value[0]

    return -1 if len(food_times) == 0 else sorted(food_times, key=lambda x: x[1])[(k-time) % len(food_times)][1]


"""
@ 세뚱이 풀이
1. (남은 음식, 인덱스) 형식으로 오름차순으로 deque로 관리
2. 최소 남은 음식의 양을 검사하여 시간 세기
3. food time 배열이 비었다면 -1 반환
4. 안 비었다면 인덱스 순으로 오름차순 정렬해서 남은 시간에 대해 순서 찾아서 반환

@ 코드 수정
1. if 문 한 줄로 변경
"""

"""
Test Case

print(solution([3, 1, 2], 5))
"""
