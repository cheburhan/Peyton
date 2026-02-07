n = int(input())

doramas = {}
for i in range(n):
    data = input().split()
    name = data[0]
    episodes = int(data[1])
    
    if name in doramas:
        doramas[name] += episodes
    else:
        doramas[name] = episodes

names = []
for name in doramas:
    names.append(name)

for i in range(len(names)):
    for j in range(i + 1, len(names)):
        if names[i] > names[j]:
            names[i], names[j] = names[j], names[i]

for name in names:
    print(name, doramas[name])