"""
괄호가 개수는 맞지만 짝이 맞지 않은 형태로
작성되어 오류가 났다.
모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램을
개발하려고 한다
다음과 같은 과정을 통해 '올바른 괄호 문자열'로 변환 할 수 있다.
1. 입력이 빈 문자열인 경우, 빈 문자열 반환
2. 문자열 w를 두개의 균형잡힌 괄호문자열 u,v로 분리
    - 단, u는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없고, v는 빈 문자열이 될 수 있다
3. 문자열 u가 올바른 괄호 문자열이라면 문자열 v에 대해 1단계부터 다시 수행
    - 수행한 결과 문자열을 u에 이어 붙인 후 반환
4. u가 '올바른 괄호 문자열'이 아니라면 다음 과정을 수행
    1. 빈 문자열에 첫 번째 문자로 '(' 붙임
    2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙임
    3. ')' 를 다시 붙임
    4. u의 첫번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
    5. 생성된 문자열 반환

@input
균현잡힌 괄호 문자열 : p
- p는 '('와 ')'로만 이루어진 문자열이며 2 <= 길이 <= 1000이하 짝수
- 문자열 p를 이루는 '('와 ')'의 개수는 항상 같다
- 만약 p가 이미 '올바른 괄호 문자열'이라면 그대로 return

@output
올바른 괄호 문자열 반환
"""
from collections import deque


def check_balance(u):
    deque_list = deque()

    balance = True
    for c in u:
        if c == '(':
            deque_list.append(c)
        else:
            if len(deque_list) == 0:
                balance = False
                break
            deque_list.pop()

    return balance


def balance_string(s):
    if s == '':
        return ''

    value_dict = {'(': 0, ')': 0}
    pos = 0
    for idx in range(0, len(s)):
        value_dict[s[idx]] += 1
        if value_dict['('] == value_dict[')']:
            pos = idx+1
            break

    u, v = (s[0:pos], '') if len(s) == pos else (s[0:pos], s[pos:])
    if check_balance(u):
        result = u + balance_string(v)
    else:
        result = '(' + balance_string(v) + ')'
        u = list(u[1:len(u)-1])

        for idx in range(0, len(u)):
            if u[idx] == '(':
                u[idx] = ')'
            else:
                u[idx] = '('
        result += ''.join(u)

    return result


def solution(p):
    return balance_string(p)


"""
@ 세뚱이 풀이
1. 문제의 주어진 알고리즘대로 코드 작성
2. 풀면서 너무 C++, Java 코드 느낌이 들었다.
3. Python 2로 채점해서 한 15분 정도 낭비했다.. 시험 때는 절대 이런 실수 하면 안됨!!
"""

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
