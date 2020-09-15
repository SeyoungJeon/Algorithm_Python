from itertools import permutations


def calculate(num1, num2, operation):
    operation_dict = {'-': num1-num2, '+': num1+num2, '*': num1*num2}
    return operation_dict[operation]


def solution(expression):
    answer = 0

    expression_list = []
    operation_set = set()

    temp_str = ''
    for chr in expression:
        if chr.isdigit():
            temp_str += chr
        else:
            expression_list.append(int(temp_str))
            expression_list.append(chr)
            operation_set.add(chr)
            temp_str = ''
    expression_list.append(int(temp_str))

    for element in permutations(operation_set):
        temp_expression_list = [value for value in expression_list]
        for operation in element:
            while operation in temp_expression_list:
                idx = temp_expression_list.index(operation)
                if temp_expression_list[idx] == operation:
                    value = calculate(temp_expression_list[idx-1], temp_expression_list[idx+1], operation)
                    for i in range(3):
                        temp_expression_list.pop(idx-1)
                    temp_expression_list.insert(idx-1, value)

        if answer < abs(temp_expression_list[0]):
            answer = abs(temp_expression_list[0])

    return answer

"""
@ 세뚱이 풀이
1. expression을 연산자 기준으로 분리된 리스트 관리
2. expression에 포함된 연산자를 permutation 구하기
3. 우선순위 순열에 따라 계산하며 최종값 중 절대값이 제일 큰 수 저장

@ 다른 사람 풀이 중 반영할 점
1. list 함수 중 index 활용하기
2. 문자열 계산 시 2가지 방법
    - eval 함수 사용
    - dictionary로 계산 결과 값 관리 
"""

print(solution("0-0*0-0+09"))

# print(solution("999+999+999+999+999+999+999+999+999+999+999+999+999+999+999+999+999+999+999+999+999+999+999+999+999"))
#print(solution("100-200*300-500+20"))
#print(solution("50*6-3*2"))