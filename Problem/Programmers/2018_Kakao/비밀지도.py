"""
비밀지도를 해독하기
지도는 한변의 길이가 n이며 각 칸은 ' ' 또는 '#'
전체지도는 두 장의 지도를 겹쳐서 얻음 (겹친 부분이 하나라도 벽이면 벽, 모두 공백이면 공백)
지도1과 지도2는 각각 정수 배열로 암호화
암호화된 배열은 지도의 벽은 1, 공백은 0으로 부호화했을 때 얻어지는 이진수 값의 배열

@input
한 변의 크기 : n  1 <= n <= 16
2개 정수 배열 : arr1, arr2 (길이 n)

@output
'#', ' '으로 구성된 문자열 배열
"""


def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        binary_data = str(bin(i | j)[2:]).zfill(n)
        answer.append(binary_data.replace('1', '#').replace('0', ' '))

    return answer

"""
@ 세뚱이 풀이
1. 배열 원소에 대해 2진수 문자열로 변환 후, zfill 활용하여 자릿수 채움
2. | 연산을 이용하여 합집합으로 벽과 공백 구분

@ 다른 사람 풀이 중 반영할 점
- arr1, arr2를 zip으로 묶어서 활용
- bin, replace 활용
"""

"""
Test Case

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
"""
