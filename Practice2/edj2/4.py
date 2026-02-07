n = int(input())
numbers = input().split()
count = 0

for i in range(n):
    if int(numbers[i]) > 0:
        count += 1

print(count)