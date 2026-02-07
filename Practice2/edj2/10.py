n = int(input())
s = input().split()

arr = []
for i in range(n):
    arr.append(int(s[i]))

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for i in range(n):
    print(arr[i], end=" ")