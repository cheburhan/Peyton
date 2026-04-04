import re
text = input()
pattern = '^[A-Za-z].*\d$'

if re.search(pattern, text):
    print("Yes")
else:
    print("No")