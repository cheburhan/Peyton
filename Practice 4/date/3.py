from datetime import datetime

current = datetime.now()
clean_time = current.replace(microsecond=0)

print(clean_time)
