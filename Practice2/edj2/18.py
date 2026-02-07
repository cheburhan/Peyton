n = int(input())

strings = []
for i in range(n):
    s = input()
    strings.append(s)

first_entry = {}
for i in range(n):
    s = strings[i]
    if s not in first_entry:
        first_entry[s] = i + 1

unique_strings = []
for s in first_entry:
    unique_strings.append(s)

for i in range(len(unique_strings)):
    for j in range(i + 1, len(unique_strings)):
        if unique_strings[i] > unique_strings[j]:
            unique_strings[i], unique_strings[j] = unique_strings[j], unique_strings[i]

for s in unique_strings:
    print(s, first_entry[s])