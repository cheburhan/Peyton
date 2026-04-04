def generator(n):
    for i in n:
        yield i * i * i

n = list(map(int,input().split()))
print(" ".join(map(str, generator (n))))