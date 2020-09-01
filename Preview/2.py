# a, b = map(int, input().strip().split(' '))
a, b = 7, 5
print(a//b, a%b)
print(*divmod(a,b))