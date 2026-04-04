import re
text = input()
def double_digit(match):
    digit = match.group(0)  
    return digit * 2  

result = re.sub(r'\d', double_digit, text)
print(result)