"""
웹 페이지 매칭 점수 계산
한 웹페이지에 기본점수, 외부 링크 수, 링크 점수, 매칭점수를 구할 수 있다
기본 점수 : 웹페이지의 텍스 중, 검색어가 등장하는 횟수 (대소문자 무시)
외부 링크 수 : 웹페이지에서 다른 외부 페이지로 연결된 링크 개수
링크 점수 : 해당 웹페이지로 링크가 걸린 다른 웹페이지의 기본 점수 / 외부 링크의 수
매칭 점수 : 기본 점수 + 링크 점수

매칭 점수가 가장 높은 웹페이지의 index 구하기
만약, 그런 페이지가 여러개라면 그 중 가장 번호가 가장적은 것 구하기

@input
HTML 형식 웹페이지가 문자열 형태로 있는 배열 : pages
- 1 <= 길이 <= 20
- 1 <= 한 웹페이지 문자열 길이 <= 1500
- 웹 페이지의 인덱스는 0부터 시작
- 한 웹페이지의 url은 meta 태그 값
- 외부 링크는 <a href
- 모든 url 은 https://로만 시작

검색어 : word
- 하나의 영어 단어, 알파벳소문자와 대문자로만 이루어짐
- 1<= 길이 <= 12
- 대소문자 구분은 무시하고 찾음
- 검색어는 단언 단위로만 비교

@output
매칭 정수 가장 높은 index, 같다면 가장 작은 index
"""
import re


def solution(word, pages):
    answer_list = []
    link_dict = {}
    url_compile = re.compile('<meta property=\"og:url\" content=\"https://(.+)\"/>')
    word_compile = re.compile('[^a-zA-Z]%s(?=[^a-zA-Z])|^%s[^a-zA-Z]|[^a-zA-Z]%s$' %(word, word, word), re.IGNORECASE)
    for idx, page in enumerate(pages):
        url = re.findall(url_compile, page)[0]
        external_link_list = [value.split('\"')[0] for value in page.split('a href=\"https://')[1:]]
        basic_point = len(re.findall(word_compile, page))
        link_dict[url] = {'external': external_link_list, 'basic': basic_point, 'num': idx}

    for key1 in link_dict:
        link_point = 0
        for key2 in link_dict:
            if key1 == key2:
                continue
            if key1 in link_dict[key2]['external']:
                link_point += (link_dict[key2]['basic'] / len(link_dict[key2]['external']))
        answer_list.append((link_dict[key1]['basic'] + link_point, link_dict[key1]['num']))

    answer_list.sort(key=lambda x: (-x[0], x[1]))

    return answer_list[0][1]

"""
@ 세뚱이 풀이
1. 정규식을 이용해서 해당 데이터를 추출
2. dictionary로 해당 데이터를 관리
3. dictionary 순회하면서 매칭 점수 계산

@ 다른 사람 풀이 참고
1. 검색어 추출하는 정규식에 문제가 있었음 (앞+뒤,뒤,앞) 3가지 경우 모두 검사했어야 했음
2. 외부 링크 추출하는데 문제가 있었음 (정규식으로 추출하려 했으나, 안되서 split으로 대체)
"""

"""
Test Case

print(solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution(	"Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
"""
