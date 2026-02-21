from datetime import datetime, timedelta

current = datetime.now()
result = current - timedelta(days=5)

print(result)
