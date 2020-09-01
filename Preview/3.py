num, base = map(int, input().strip().split(' '))

print(int(str(num), base))

answer = 0
for idx, i in enumerate(str(num)[::-1]):
    answer += int(i) * (base ** idx)
print(answer)