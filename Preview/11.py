import itertools


def solution(mylist):
    mylist.sort()
    answer = list(map(list, itertools.permutations(mylist)))
    return answer


print(solution([1, 2]))