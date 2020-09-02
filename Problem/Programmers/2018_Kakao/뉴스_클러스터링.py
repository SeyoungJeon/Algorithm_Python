"""
자카드 유사도 = 두 집합의 교집합 크기를 두 집합의 합집합 크키로 나눈 값 (단, A,B가 모두 공집합 일 경우 값은 1)
@input
str1, str2 (길이는 2이상 1000이하)
두 글자씩 끊어서 다중집합의 원소로 만듦 (영문자로 된 글자쌍만 유효, 대문자와 소문자의 차이 무시)

@output
(유사도 값 * 65536) 소수점 아래 버림
"""


def solution(str1, str2):
    str1_list = [str1[idx:idx+2].lower() for idx in range(0, len(str1) - 1) if str1[idx:idx+2].isalpha()]
    str2_list = [str2[idx:idx+2].lower() for idx in range(0, len(str2) - 1) if str2[idx:idx+2].isalpha()]

    if len(str1_list) == 0 and len(str2_list) == 0:
        return 65536

    inter_set = set(str1_list) & set(str2_list)
    union_set = set(str1_list) | set(str2_list)

    inter_sum = sum([min(str1_list.count(value), str2_list.count(value)) for value in inter_set])
    union_sum = sum([max(str1_list.count(value), str2_list.count(value)) for value in union_set])

    return int((inter_sum/union_sum) * 65536)

"""
다른 사람 풀이 반영 할 점
- 다중 집합에 대한 교집합과 합지합을 구할 경우, 일반 교집합과 합집합을 먼저 만든 후, count로 구하기
- list 선언 시 한 번에 선언 함 e.g.) [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
- 교칩합 합집합 구할 때, Counter 사용 혹은 set으로 변환하여 중복된 것을 세기
- math floor 함수 대신에 int로 형변환해서 소수점 버릴 수 있음
"""

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
