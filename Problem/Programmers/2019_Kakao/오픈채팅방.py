"""
오픈채팅방에 다양한 사람들이 드나드는 것을 지켜볼 수 있는 관리자창을 만들기로 했다
[닉네임]님이 들어왔습니다.
[닉네임]님이 나갔습니다.

닉네임 변경 방법 2가지
1. 채팅방을 나간 후, 새로운 닉네임으로 다시 들어감
2. 채팅방에서 닉네임 변경
닉네임 변경 시 기존에 채팅방에 출력되어 있던 메시지 전부 변경

채팅방 중복 닉네임 허용

@input
문자열 배열 : record (1 <= len(record) <= 100000)
- 모든 유저는 [유저 아이디로] 구분
= Enter uid1234 Muzi
- Leave uid1234
- Change uid1234 Muzi
- 첫 단어는 Enter, Leave, Change 중 하나
- 각 단어는 공백으로 구분, 알파멧 대소문자, 숫자로만 구성
- 유저 아이디와 닉네임은 알파벳 대소문자 구별
- 유저아이디와 닉네임 길이는 1이상 10 이하

@output
최종적으로 방을 개설한 사람이 보게되는 메시지 묹자열 배열
"""


def solution(record):
    answer = []
    command_dict = {'Enter': '들어왔습니다.', 'Leave': '나갔습니다.'}
    user_dict = {}
    for value in record:
        value = value.split(' ')
        if value[0] != 'Leave':
            user_dict[value[1]] = value[2]

    for value in record:
        value = value.split(' ')
        if value[0] != 'Change':
            answer.append(user_dict[value[1]] + '님이 ' + command_dict[value[0]])

    return answer


"""
@ 세뚱이 풀이
1. command에 대한 dict 선언
2. user에 대한 dict를 선언하여 닉네임의 변경사항을 순차적으로 수정할 수 있었다.
"""

print(solution(	["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))