import re
text = input()

words = re.findall('\w+', text)

print(len(words))