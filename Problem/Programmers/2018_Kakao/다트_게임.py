"""
다트판에 다트를 3차례 던져 점수의 합계로 겨루는 게임
점수 계산 로직
1. 각 기회마다 점수 0 ~ 10
2. Single 1제곱, Double 2제곱, Triple 3제곱
3. 스타상(*) : 해당 점수와 바로 전에 얻은 점수를 각 2배
4. 아차상(#) 해당 점수 마이너스
5. 스타상은 첫 번째에도 나오는 이 때 해당 점수만 2배
6. 스타상은 다른 스타당과 중첩될 수 있고 이 경우 점수 4배
7. 스타상과 아차상 효과 중첩 이 경우 점수 -2배
8. Single, Double, Triple은 점수 마다 하나씩 존재
9. 스타상과 아차상은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수 있음

@input
점수|보너스|[옵션] (문자열 형식)
- 0 <= 점수 <= 10
- 보너스는 S,D,T 중 하나
- 옵션은 * 혹은 # 이며, 없을 수 있음

@output
점수값
"""


def solution(dartResult):
    num_str = ''
    alpha_dict = {'S': 1, 'D': 2, 'T': 3}
    point_list = []
    for idx, value in enumerate(dartResult):
        if value.isdigit():
            num_str += value
        elif value.isalpha():
            point_list.append(pow(int(num_str), alpha_dict[value]))
            if idx + 1 >= len(dartResult):
                break

            if not (dartResult[idx+1] == '*' or dartResult[idx+1] == '#'):
                num_str = ''
        else:
            if value == '*':
                if len(point_list) > 1:
                    point_list[len(point_list) - 2] *= 2
                point_list[len(point_list) - 1] *= 2
            else:
                point_list[len(point_list) - 1] *= -1

            num_str = ''

    return sum(point_list)

"""
@ 세뚱이 풀이
1. 반복문 하나에서 숫자,문자,특수문자인지 구분
2. 숫자인 모으고 문자인경우 해당 문자에 따라 점수를 리스트에 추가
3. 특수 문자인 경우 리스트 길이에 따라 처리

푸는데 1시간 정도 걸렸는데, 좀 더 빨리 풀 수 있는 것을 오래 걸린 것 같다..
- 처음에 문제 파악이 제대로 안됬음 -> 해결 방법을 도중에 수정 

문제를 제대로 파악하고 접근하자
"""

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))
