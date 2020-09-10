"""
문자열 압축
단위 별로 잘라서 압축을 시켜서 제일 짧은 문자열의 길이를 반환

@input
문자열 : s
- 1 <= 길이 <= 1000
- 소문자로만 구성

@output
압축해 표현한 문자열 중 가장 짧은 길이
"""


def solution(s):
    answer = float('inf')
    max_len = len(s) // 2 if len(s) % 2 == 0 else len(s) // 2 + 1
    for i in range(1, max_len+1):
        string_list = [s[j:j+i] for j in range(0, len(s), i)]
        compression_string = ''
        value, count = string_list[0], 1
        for idx in range(1, len(string_list)):
            if value == string_list[idx]:
                count += 1
            else:
                compression_string += str(count) + value if count > 1 else value
                count = 1
                value = string_list[idx]
        compression_string += str(count) + value if count > 1 else value
        answer = min(answer, len(compression_string))

    return answer

"""
@ 세뚱이 풀이
1. 자를 수 있는 최대 길이 구하기
2. 1 부터 자를 수 있는 최대 길이까지 반복하면서 문자열 잘라서 저장
3. 자른 문자열을 기준으로 원래 문자열과 비교하며 압축 문자의 개수 세기
4. 압축 개수 세어서 압축 문자열 만든 후, 최솟값 저장
"""
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))