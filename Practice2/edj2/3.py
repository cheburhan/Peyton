a = int(input())
arr = list(map(int, input().split()))
s = 0
for i in range(a):
    s += arr[i]
print(s)