n = int(input())
s = input().split()

seen = []
for i in range(n):
    num = s[i]
    if num not in seen:
        print("YES")
        seen.append(num)
    else:
        print("NO")