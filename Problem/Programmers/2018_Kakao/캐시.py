"""
DB 캐시 적용 시,
캐시 크기에 따른 실행시간 측정 프로그램 만들기

캐시 알고리즘 (LRU)
hit : 실행시간 1
miss : 실행시간 5

@input
캐시 크기 : cacheSize 0 <= cacheSize <= 30
도시이름 배열 : cities (max : 100000) 영문자로만 구성, 대소문자 구분 X, 도시 이름은 최대 20자

@output
총 실행시간
"""
from _collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache_list = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache_list:
            answer += 1
            cache_list.remove(city)
            cache_list.appendleft(city)
        else:
            answer += 5
            cache_list.appendleft(city)

    return answer

"""
@ 세뚱이 풀이
1. city 소문자로 변경된 리스트 선언 및 deque 형식의 cache 선언
2. 해당 city가 있을 경우 실행시간 추가 1, 해당 원소 삭제 후 앞에 추가
3. 해당 city가 없을 경우 실행시간 추가 5, 해당 원소 추가 후, 만약 캐쉬길이보다 크면 마지막 원소 삭제

@ 다른 사람 풀이 참고하여 반영할 점
1. 따로 소문자로 된 도시 리스트 만들지말고 반복문 돌릴 때 처리
2. deque 최대 길이 값 설정
3. in 을 통해서 데이터 삭제 및 추가
"""

"""
Test Case

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
"""
