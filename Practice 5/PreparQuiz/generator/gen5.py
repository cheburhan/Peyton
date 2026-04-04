def generator(numbers):
    global n
    for i in numbers:
        if i > n:
            yield i

n = int(input())
b = list(map(int, input().split()))
print(" ".join(map(str, generator(b))))