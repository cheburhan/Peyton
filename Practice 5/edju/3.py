import re
text = input()
pattern = input()
m = re.findall(pattern, text)
print(len(m))