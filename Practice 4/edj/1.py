n = int(input())
def squares(n):
    for i in range(1, n+1):
        yield i**2

for val in squares(n):
    print(val)
