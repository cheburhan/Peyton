import re


text = input()  
pattern = input()  

# Escape any regex metacharacters in the pattern
escaped_pattern = re.escape(pattern)

# Compile the pattern and find all occurrences
compiled_pattern = re.compile(escaped_pattern)
matches = compiled_pattern.findall(text)

# Count the matches
count = len(matches)

# Output the result
print(count)