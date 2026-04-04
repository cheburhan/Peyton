def squares(numbers):
    for i in numbers:
        yield i * i

n = list(map(int, input("Введите числа: ").split()))


print(" ".join(map(str, squares(n))))