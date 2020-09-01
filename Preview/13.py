def solution(mylist):
    answer = []
    for value in mylist:
        if value % 2 == 0:
            answer.append(value**2)
    return answer


def solution(mylist):
    answer = [value**2 for value in mylist if value % 2 == 0]
    return answer