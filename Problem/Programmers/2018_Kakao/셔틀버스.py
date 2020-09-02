"""
셔틀 버스 규칙
1. 9시부터 총 n회 t분 간격을 도착 (최대 m명 탑승)
2. 셔틀 버스 도착한 순간 대기열에 선 크루까지 포함해서 순서대로 태움 (셔틀버스 9시 도착, 크루 9시 도착 자리가 있다면 타고감)

셔틀타고 사무실로 갈 수 있는 도착 시간 중 제일 늦은 시각 구하기
(같은 시간에 도착한 크루가 있다 하더라도 맨 마지막에 줄을 선다)

@input
셔틀 운행 횟수 : n    0 < n <= 10
셔틀 운행 간격 : t    0 < t <= 60
최대 탑승 수 : m     0 < m <= 45
크루 도착 시간 배열 : timetable     1 <= 길이 < 2000 (HH:MM , 00:01 ~ 23:59)

@output
제일 늦은 도착 시각 : HH:MM 형식
"""


def solution(n, t, m, timetable):
    timetable_second = [int(time[0:2]) * 60 + int(time[3:5]) for time in timetable]
    timetable_second.sort()

    time, pos = 540, 0  # 배차 시간, 탑승된 크루 위치
    for i in range(n):
        count = 0   # 한 배차 간격 당 탑승 인원 수
        for j in range(m):
            if 0 <= pos < len(timetable_second) and timetable_second[pos] <= time:
                count += 1
                pos += 1
            else:
                break

        # 최대 탑승 인원 인 경우 마지막 탑승 인원 시간 -1, 아닌 경우 배차 시간
        last = timetable_second[pos-1] - 1 if count == m else time
        time += t

    answer = '%02d:%02d' % (last//60, last%60)

    return answer


"""
@ 세뚱이 풀이
1. 주어진 시간을 분으로 변환한 후, 오름차순 정렬
2. 운행 횟수 반복문 -> 탑승 인원 수 반복문(탑승 인원 카운트)
    -> 최대 탑승 인원일 경우, 마지막 탄 사람보다 -1, 아닌 경우 배차 시간
3. zfill, %02d 이용해서 2자리 수 표현
"""

"""
@ Test Case
print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45,
               ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                "23:59", "23:59", "23:59", "23:59", "23:59"]))
"""
