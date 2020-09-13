import re


def solution(new_id):
    answer = ''
    lower_new_id = new_id.lower()

    for value in lower_new_id:
        if value.isalnum() or re.search('[-_.]', value):
            answer += value

    answer = re.sub('[.]+', '.', answer)

    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) <= 2:
        last = answer[-1]
        while len(answer) < 3:
            answer += last

    return answer