import re
text = input()
s = input()
if re.search(s, text):
    print("Yes")
else:
    print("No")