from collections import deque


def solution(ball, order):
    answer = []
    ball = deque(ball)
    manage_order = set()

    for num in order:
        while len(manage_order):
            if ball[0] in manage_order:
                answer.append(ball.popleft())
            elif ball[len(ball) - 1] in manage_order:
                answer.append(ball.pop())
            else:
                break

        if ball[0] == num:
            answer.append(ball.popleft())
        elif ball[len(ball)-1] == num:
            answer.append(ball.pop())
        else:
            manage_order.add(num)

    return answer


# print(solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]))
print(solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]))