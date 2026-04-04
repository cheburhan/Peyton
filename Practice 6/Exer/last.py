from functools import reduce

nums = [1, 2, 3, 4, 5]

mapped = list(map(lambda x: x * 2, nums))
filtered = list(filter(lambda x: x % 2 == 0, nums))
reduced = reduce(lambda x, y: x + y, nums)

print(mapped)
print(filtered)
print(reduced)

names = ["a", "b", "c"]
values = [10, 20, 30]

for i, name in enumerate(names):
    print(i, name)

for n, v in zip(names, values):
    print(n, v)

x = "123"
y = int(x)
z = float(y)

print(type(x), type(y), type(z))