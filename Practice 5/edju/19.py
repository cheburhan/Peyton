import re
text = input().strip()

pattern = re.compile('\b\w+\b')

words = pattern.findall(text)
word_count = len(words)

print(word_count)