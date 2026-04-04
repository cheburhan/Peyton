import re

def kvad(numbers):
    for i in numbers:
        return i * i

text = input()
pattern = r'\d'
print(" ".join(map(str, kvad(re.findall(pattern, text)))))