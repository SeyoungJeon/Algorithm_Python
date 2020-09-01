# 야근 피로도 계산
"""
남은 시간 N
작업량 리스트 works
피로도 = 작업량 제곱의 합
최소 피로도 값 반환
"""

import heapq


def solution(n, works):
    max_heap = []
    for work in works:
        heapq.heappush(max_heap, -work)

    while n > 0:
        value = -heapq.heappop(max_heap) - 1
        n -= 1

        if value > 0:
            heapq.heappush(max_heap, -value)
        else:
            heapq.heappush(max_heap, 0)

    answer = sum(value**2 for value in max_heap)

    return answer


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
