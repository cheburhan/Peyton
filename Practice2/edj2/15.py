n = int(input())
unique = {}
for i in range(n):
    surname = input().strip()
    unique[surname] = 1
print(len(unique))
