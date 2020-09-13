"""
코스요리 형태로 재구성
최소 2가지 이상 단품메뉴

각 단품메뉴 A~Z 대문자 표기
"""
from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []

    course_dict = defaultdict(int)
    for order in orders:
        for i in range(2, len(order)+1):
            for comb in combinations(order, i):
                comb = sorted(comb)
                key = ''
                for chr in comb:
                    key += chr

                course_dict[key] += 1

    for element in course:
        course_list = []
        for key in course_dict:
            if len(key) == element and course_dict[key] >= 2:
                course_list.append((key, course_dict[key]))
        course_list.sort(key=lambda x: -x[1])
        if len(course_list) == 0:
            continue

        max_value = course_list[0][1]
        for value in course_list:
            if value[1] != max_value:
                break
            answer.append(value[0])

    return sorted(answer)

#print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
