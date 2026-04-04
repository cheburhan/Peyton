def generator (numbers):
    for i in numbers:
        if i%2 == 0:
            yield i
        

n = list(map(int, input().split()))
print(" ".join(map(str, generator(n))))