n = int(input())
s = input().split()

arr = []
for i in range(n):
    arr.append(int(s[i]))

count = {}
for num in arr:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

max_count = 0
result = float('inf')

for num in count:
    if count[num] > max_count or (count[num] == max_count and num < result):
        max_count = count[num]
        result = num

print(result)