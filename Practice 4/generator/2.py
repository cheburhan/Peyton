n = int(input())

def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

print(",".join(str(num) for num in even_generator(n)))
