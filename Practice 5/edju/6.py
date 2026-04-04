import re
text = input()
pattern = '\S+@\S+\.\S+'
match = re.search(pattern, text)

if match:
    print(match.group())
else:
    print("No email")