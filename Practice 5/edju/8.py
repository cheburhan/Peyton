import re
text = input()       
d = input() 
p = re.split(d, text)
print(','.join(p))