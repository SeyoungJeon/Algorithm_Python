from collections import deque


def solution(cards):
    answer = -1
    player, dealer = [], []
    cards = deque(cards)

    player.append(cards.popleft())
    player.append(cards.popleft())

    while True:
        zero_count = player.count(0)
        value = sum(player)








    return answer


print(solution([12, 7, 11, 6, 2, 12]))
print(solution([1, 4, 10, 6, 9, 1, 8, 13]))
print(solution([10, 13, 10, 1, 2, 3, 4, 5, 6, 2]))
print(solution([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))