n = int(input())
s = input().split()

max_num = int(s[0])
max_pos = 1

for i in range(1, n):
    num = int(s[i])
    if num > max_num:
        max_num = num
        max_pos = i + 1

print(max_pos)