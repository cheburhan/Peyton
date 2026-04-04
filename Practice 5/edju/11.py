import re
text = input()
uplet = re.findall('[A-Z]', text)
#символьный класс котрый находит от A-Z
print(len(uplet))