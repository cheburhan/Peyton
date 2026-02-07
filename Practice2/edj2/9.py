n = int(input())
s = input().split()

arr = []
for i in range(n):
    arr.append(int(s[i]))

max_num = arr[0]
min_num = arr[0]

for i in range(1, n):
    if arr[i] > max_num:
        max_num = arr[i]
    if arr[i] < min_num:
        min_num = arr[i]

for i in range(n):
    if arr[i] == max_num:
        arr[i] = min_num

for i in range(n):
    print(arr[i], end=" ")