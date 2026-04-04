import re
text = input()
digits = re.findall('\d', text)
if digits:
    print(' '.join(digits))
else:
    print()