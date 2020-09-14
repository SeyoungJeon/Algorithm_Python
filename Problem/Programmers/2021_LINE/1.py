from collections import defaultdict


def solution(boxes):
    answer = 0

    box_dict = defaultdict(int)
    for box in boxes:
        box_dict[box[0]] += 1
        box_dict[box[1]] += 1

    wrapped_box = 0
    for key in box_dict:
        if box_dict[key] % 2 != 0:
            answer += 1
        else:
            wrapped_box += 1

    if len(boxes) < answer + wrapped_box:
        answer = len(boxes) - wrapped_box

    return answer


print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))
print(solution([[1, 2], [2, 3], [3, 1]]))
print(solution([[1, 2], [3, 4], [5, 6]]))