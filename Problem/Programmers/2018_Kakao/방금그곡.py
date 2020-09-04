"""
방금그곡에서는 TV, 라디오 등에서 나온 음악에 관해 제목 등의 정보를 제공하는 서비스
네오는 기억한 멜로디를 재생시간과 제공된 악보를 직접 보면서 비교하려고 한다.
네오가 찾으려는 음악의 제목을 구하라

음악제목,재생이 시작되고 끝난 시각, 악보 제공
음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개
각 음은 1분에 1개씩 재생 (반드시 처음부터 재생)
음악 길이보다 재생된 시간이 길때는 음악이 끊김 없이 처음부터 반복해서 재생,
음악 길이보다 재생된 시간이 짧을때는 처음부터 재생 시간 만큼 재생
00:00를 넘겨서까지 재생되는 일은 없음
조건이 일치하는 음악이 여러개인 경우 재생된 시간이 제일 긴 음악 제목 반환, 재생시간도 같을 경우 먼저 입력된 음악 제목 반환
조건이 일치하는 음악 없을때는 None을 반환

@input
멜로디를 담은 문자열 : m (1<= m <= 1439)
곡 정보 배열 : musicinfos (길이 100 이하)
- 시작 시각 (24시간 형식 HH:MM)
- 끝난 시각 (24시간 형식 HH:MM)
- 음악 제목 (음악제목은 1~64 문자열)
- 악보 정보 (1 <= 악보 정보 <= 1439)

@output
조건과 일치하는 음악 제목
"""


def solution(m, musicinfos):
    answer_list = []
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(',')
        melody = melody.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        dif = int(end.split(':')[0]) * 60 + int(end.split(':')[1]) - int(start.split(':')[0]) * 60 + int(start.split(':')[1])
        divide = divmod(dif, len(melody))
        divide = divide[0] + 1 if divide[1] > 0 else divide[0]

        melody = melody[0:dif] if len(melody) > dif else melody * divide

        if m in melody:
            answer_list.append((dif, title))

    answer = '(None)' if len(answer_list) == 0 else sorted(answer_list, key=lambda x: (-x[0]))[0][1]

    return answer

"""
@ 세뚱이 풀이
1. 문자열 replace를 통해 # 부분을 처리
2. HH:MM 형식을 단위 분으로 변환
3. sorted 함수에서 lamda를 이용한 재생시간 오름차순 정렬

@ 다른 사람 풀이에서 반영할 점
1. sorted(musicinfos_init, key=lambda music:music[4], reverse = True) 
  - 오름차순 정렬할 때, reverse 키워드 사용
2. 음악 제목과, 재생길이를 따른 리스트에 관리하여 titles[musics.index(max(musics))]
  - 정렬하지 않고 최대 재생길이 인덱스를 찾아 음악제목을 반환한다
3. 미리 변경할 문자들을 사전으로 관리해서 for문 형식으로 replace 해도 된다
"""

# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABCDEFG", ["23:50,00:04,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))