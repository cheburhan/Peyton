def generator (n):
    for i in range (1, n+1):
        yield i

n = int(input())
gen = generator(n)
print(" ".join(map(str, generator(n))))