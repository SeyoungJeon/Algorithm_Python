s, n = input().strip().split(' ')

middle = (int(n) - len(s)) // 2
last = int(n) - len(s)

answer = s + '\n' + (' ' * middle) + s + '\n' + (' ' * last) + s + '\n'
# print(answer)


# 문자열 정렬
print(s.ljust(int(n)))
print(s.center(int(n)))
print(s.rjust(int(n)))