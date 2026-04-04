import re
text = input()

# Pattern with capturing groups for name and age
# Name: (.*?), Age: (.*)
# .*? non-greedy match for name
# .* match for age (rest of the string)
pattern = r'Name:\s*(.*?),\s*Age:\s*(.*)'

match = re.search(pattern, text)

if match:
    name = match.group(1).strip()
    age = match.group(2).strip()
    print(f"{name} {age}")