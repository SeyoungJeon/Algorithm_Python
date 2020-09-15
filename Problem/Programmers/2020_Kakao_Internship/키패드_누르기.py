def solution(numbers, hand):
    answer = ''

    left, right = 9, 11
    for number in numbers:
        if number == 0:
            number = 11

        number -= 1

        if number == 0 or number == 3 or number == 6:
            left = number
            answer += 'L'
        elif number == 2 or number == 5 or number == 8:
            right = number
            answer += 'R'
        else:
            pos_left = divmod(left, 3)
            pos_right = divmod(right, 3)
            pos_cur = divmod(number, 3)

            left_distance = abs(pos_cur[0] - pos_left[0]) + abs(pos_cur[1] - pos_left[1])
            right_distance = abs(pos_cur[0] - pos_right[0]) + abs(pos_cur[1] - pos_right[1])

            if left_distance == right_distance:
                if hand == "left":
                    left = number
                    answer += 'L'
                else:
                    right = number
                    answer += 'R'
            else:
                if left_distance < right_distance:
                    left = number
                    answer += 'L'
                else:
                    right = number
                    answer += 'R'

    return answer


"""
@ 세뚱이 풀이
1. 각 숫자를 몫과 나머지를 구해서 좌표를 만들어서 왼쪽과 오른쪽을 판단했다.

@ 다른 사람 풀이 중 반영할 점
1. 각 숫자에 대한 좌표를 미리 dictionary로 가지고 있다가 해당 숫자가 나오면 해당 좌표로 계산한다.
- 몫과 나머지를 계산하면서 거리를 구할 필요가 없어서 빨리 풀 수 있다.
- 나같은 경우는 방금 몫과 나머지로 좌표를 구하면서 시간을 좀 뺏겼다.
"""

"""
Test Case

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
"""
