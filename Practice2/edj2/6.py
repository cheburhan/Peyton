n = int(input())
s = input().split()

max_num = int(s[0])
for i in range(1, n):
    num = int(s[i])
    if num > max_num:
        max_num = num

print(max_num)