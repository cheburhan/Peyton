import re
text = input()        
pattern = input()     
rep= input()

#escape - экранирует все regex-метасимволы в паттерне:
#Если паттерн содержит символы типа ., *, +, ?, [, ], (, ), {, }, \, |, ^, $
#Превращает их в literal символы (например, "." → "\.")
esc = re.escape(pattern)
result = re.sub(esc, rep, text)

print(result)