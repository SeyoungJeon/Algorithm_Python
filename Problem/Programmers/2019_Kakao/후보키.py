"""
후보키에 대한 고민이 필요
- 유일하게 식별할 수 있는 속성 
   - 유일성
   - 최소성
학생들의 인적사항이 주어졌을 때, 후보키의 최대 개수 구하기

@input
relation
- 2차원 문자열 배열
- 컬럼의 길이는 1 이상 8이하
- 로우의 길인느 1 이상 20이하
- 모든 문자열의 길이는 1 이상 8이하며 알파벳과 소문자와 숫자로만 이루어짐
- 중복되는 튜플은 없음

@output
후보키의 개수
"""
from itertools import combinations


def solution(relation):
    answer = 0

    elements_list = []
    idx_list = [i for i in range(len(relation[0]))]

    for i in range(1, len(relation[0])):
        combinations_list = list(combinations(idx_list, i))

        for elements in combinations_list:
            data_set = set()
            for value in relation:
                data_set.add(tuple([value[element] for element in elements]))

            if len(data_set) == len(relation):
                elements_list.append([elements, False])

    for idx in range(0, len(elements_list)):
        if elements_list[idx][1]:
            continue

        for idx2 in range(idx+1, len(elements_list)):
            for element in elements_list[idx][0]:
                if element in elements_list[idx2][0]:
                    elements_list[idx2][1] = True
                    break
    for value in elements_list:
        if not value[1]:
            answer += 1

    return answer

"""
@ 세뚱이 풀이
1. combinations을 활용해 조합 경우의 수를 모두 구한다.
2. len()과 set()을 이용해 중복이 되었는지 안되었는지 확인한다.
3. 중복이 안되는 조합만 리스트로 관리하여, 최소성을 만족하도록 수정했다.
"""

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))