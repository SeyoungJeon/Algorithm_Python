# 내가 작성한 코드
def solution(mylist):
    answer = []
    for list in mylist:
        answer.append(len(list))

    return answer


# 권장하는 코드
def solution(mylist):
    return list(map(len, mylist))


print(solution([[1], [2]]))