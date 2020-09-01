import collections

my_str = input().strip()

answer = collections.Counter(my_str)

alpha_list = []

max_value = 0
for key in answer:
    if max_value < answer[key]:
        max_value = answer[key]

for key in answer:
    if answer[key] == max_value:
        alpha_list.append(key)

an = sorted(alpha_list)
print(''.join(an))