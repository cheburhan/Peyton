n = int(input())

contacts = []
for i in range(n):
    contact = input()
    contacts.append(contact)

count = {}
for contact in contacts:
    if contact in count:
        count[contact] += 1
    else:
        count[contact] = 1

result = 0
for contact in count:
    if count[contact] == 3:
        result += 1

print(result)