import string

num = int(input().strip())


if num == 0:
    start = ord('a')
else:
    start = ord('A')

for i in range(0,26):
    print(chr(start+i), end = '')

# 권장
if num == 0:
    print(string.ascii_lowercase)
else:
    print(string.ascii_uppercase)
