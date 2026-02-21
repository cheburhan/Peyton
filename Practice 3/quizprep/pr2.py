num = list(map(int, input().split()))
x = {}
for i in num:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1

print (x)