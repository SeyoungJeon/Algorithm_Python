"""
동아리에서 하는 게임 규칙은 다음과 같다.
1. 숫자를 0부터 시작해서 말한다. (첫번째사람: 0 ~ 10번째사람: 9)
2. 10 이상의 숫자부터는 한 자리씩 끊어서 말한다 (11번째사람은 1 , 12번째사람은 0)

이진법에서 십육진법까지 모든 진법으로 게임을 진행
자신이 말해야하는 숫자를 스마트폰에 미리 출력해주는 프로그램을 만든다.

@input
진법 : n (2 <= n <= 16)
미리 구할 숫자의 개수 : t (0 < t <= 1000)
게임에 참가하는 인원 : m (2<= m <= 100)
튜브의 순서: p (1<= p <=m)

@output
말해야하는 숫자 t개를 공백 없이 차례대로 나타낸 문자열
(10~15는 A~F로 대체)
"""


def convert_10_to_N(number, base):
    result = '' if number > 0 else '0'
    while number > 0:
        result = str(number % base).replace('10', 'A').replace('11', 'B').replace('12', 'C').\
            replace('13', 'D').replace('14', 'E').replace('15', 'F') + result
        number //= base

    return result


def solution(n, t, m, p):
    str_data = ''.join([convert_10_to_N(idx, n) for idx in range(0, t*m)])
    answer = ''.join([str_data[i] for i in range(p-1, len(str_data), m)])
    return answer[0:t]


"""
@ 세뚱이 풀이
1. t*m 만큼 반복문 돌리면서 해당 숫자들을 n진수로 변환
2. 변환한 숫자 리스트들을 한 string으로 변환
3. 그 중에서 자신의 순서에 말할 문자만 추출해서 string으로 구성
"""

"""
Test Case

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
"""
