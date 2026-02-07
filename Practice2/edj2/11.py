n_l_r = input().split()
n = int(n_l_r[0])
l = int(n_l_r[1])
r = int(n_l_r[2])

s = input().split()
arr = []
for i in range(n):
    arr.append(int(s[i]))

l -= 1
r -= 1

while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1

for i in range(n):
    print(arr[i], end=" ")