def solution(mylist):
    answer = []

    for i in range(len(mylist)):
        temp = []
        for j in range(len(mylist)):
            temp.append(mylist[j][i])
        answer.append(temp)

    return answer


def solution2(mylist):
    return list(map(list, zip(*mylist)))


print(solution2([[1,2,3],[4,5,6],[7,8,9]]))
