"""
자카드 유사도 = 두 집합의 교집합 크기를 두 집합의 합집합 크키로 나눈 값 (단, A,B가 모두 공집합 일 경우 값은 1)
@input
str1, str2 (길이는 2이상 1000이하)
두 글자씩 끊어서 다중집합의 원소로 만듦 (영문자로 된 글자쌍만 유효, 대문자와 소문자의 차이 무시)

@output
(유사도 값 * 65536) 소수점 아래 버림
"""
import math


def make_set_list(str_data):
    str_list = []

    for idx in range(0, len(str_data) - 1):
        value = str_data[idx:idx + 2]
        if value.isalpha():
            str_list.append((value.upper(), False))

    return str_list


def solution(str1, str2):
    str1_list, str2_list = make_set_list(str1), make_set_list(str2)

    inter_count, union_count = 0, 0
    for idx1, value1 in enumerate(str1_list):
        if value1[1]:
            continue
        for idx2, value2 in enumerate(str2_list):
            if value2[1]:
                continue

            if value1 == value2:
                inter_count += 1
                temp_str1, temp_str2 = list(value1), list(value2)
                temp_str1[1], temp_str2[1] = True, True
                str1_list[idx1], str2_list[idx2] = tuple(temp_str1), tuple(temp_str2)
                break

    union_count = len(str1_list) + len(str2_list) - inter_count
    if inter_count or union_count:
        answer = math.floor(65536 * (inter_count/union_count))
    else:
        answer = 65536

    return answer

"""
다른 사람 풀이
- list 선언 시 한 번에 선언 함 e.g.) [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
- 교칩합 합집합 구할 때, Counter 사용 혹은 set으로 변환하여 중복된 것을 세기
"""

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
