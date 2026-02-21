nums = list(map(int, input().split()))
a = 0
d = 0
b = len(nums)
for i in range (len(nums)):
    a += nums[i]
c = a/b
for i in nums:
    if i > c:
        d += 1

print (d)