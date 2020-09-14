def solution(n):
    n = str(n)

    if len(n) == 0:
        return [0, n]

    count = 0
    while len(n) > 1:
        q = len(n) // 2
        left_num, right_num = n[:q], n[q:]

        pos_right = 0
        while pos_right < len(right_num) and right_num[pos_right] == '0':
            pos_right += 1

        if pos_right == len(right_num):
            left_num, right_num = left_num + right_num[:pos_right-1], right_num[pos_right-1:]
        else:
            left_num, right_num = n[:len(left_num) + pos_right], n[len(left_num) + pos_right:]

        n = str(int(left_num) + int(right_num))
        count += 1

    return [count, int(n)]


print(solution(74325))
print(solution(1000))
print(solution(10007))
print(solution(9))