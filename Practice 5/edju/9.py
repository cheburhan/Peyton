import re
text = input()
tlw = re.findall('\b\w{3}\b', text)
print(len(tlw))