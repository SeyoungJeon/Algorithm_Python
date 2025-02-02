# 추석 트래픽
"""
초당 최대 처리량 = (응답 완료 여부 관계없이) 임의 시간부터 1초(=1000밀리초)간 처리하는 요청의 최대 개수
lines (1 <= N <= 2000) 문자열
응답 완료 시간 S, 처리시간 T 공백으로 구분

"""


def solution(lines):
    answer = 0

    time_list = []

    for line in lines:
        date, response, process_time = line.split(' ')
        time = response.split(':')
        start_second = int(time[0]) * 3600000 + int(time[1]) * 60000 + float(time[2]) * 1000 - float(process_time[:-1]) * 1000 + 1
        end_second = start_second + float(process_time[:-1]) * 1000 - 1
        time_list.append((int(start_second), int(end_second)))

    for idx1, value1 in enumerate(time_list):
        start_count, end_count = 1, 1
        base_start, base_end = value1

        for idx2 in range(idx1 + 1, len(time_list)):

            comp_start, comp_end = time_list[idx2]
            
            # 시작 시간 기준
            if not (comp_end < base_start - 1000 or base_start + 1000 <= comp_start):
                start_count += 1

            # 끝 시간 기준
            if not (comp_end < base_end - 1000 or base_end + 1000 <= comp_start):
                end_count += 1

        answer = max(answer, max(start_count, end_count))

    return answer

"""
힌트
- 시간 단위를 milsec에서 1000을 곱해서 단위 변환을 더 편하게 할 수 있음
- 구간 비교할 때, 해당 구간이 아닌 것을 이용하라
e.g.) not (duration[1] < start or duration[0] >= end):
"""

"""
Test Case
print(solution(	["2016-09-15 00:00:00.000 3s"])
print(solution(	["2016-09-15 23:59:59.999 0.001s"])
print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
                "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
                "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s",
                "2016-09-15 21:00:02.066 2.62s"]))
print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))
"""
