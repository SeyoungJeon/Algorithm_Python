"""
파일명에 포함된 숫자를 반영한 정렬 기능 프로그램 구현
파일명은 100글자 이내, 영문 대소문자, 숫자, 공백, 마침표, 빼기 부호(-)만으로 이루어짐
파일은 영문자로 시작하며, 숫자를 하나 이상 포함
파일명 (HEAD,NUMBER,TAIL)
- HEAD는 숫자가 아닌 문자로만 이루어져있음
- NUMBER은 슷지로만
- TAIL은, 숫자가 다시나타날 수 있꼬 아무글자도 없을 수 있음

다음 기준으로 파일명을 ㅓㅈㅇ렬
1. HEAD부분 기준으로 사전 정렬 (대소문자 구분X)
2. HEAD가 같을 경우 숫자 순으로 정렬
3. HEAD와 NUMBER 숫자도 같을 경우 입력 순서 유지

@input
파일명 배열 : files (길이 1000 이하)
- 각 파일명은 100글자 이하
- 중복된 파일명은 없음

@output
정렬된 배열
"""
import re


def solution(files):
    answer = [re.findall("([^0-9]+)(\d+)([^_]*)", file)[0] for file in files]
    return list(map(''.join, sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))))

"""
@ 세뚱이 풀이
1. 정규식을 활용해서 Head, Number, Tail 추출
2. lamda 이용해서 정렬을 하는데, head 문자를 모두 소문자로 변동시켜서 대문자일 경우게도 같게 처리했고
   head가 같을 경우 number를 이용해서 정렬

@ 다른 사람 풀이 중에서 반영할 점
1. [] 안에 for문 삽입하여 list 간단하게 만들기 
"""

"""
Test Case

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
"""
