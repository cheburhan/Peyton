from datetime import datetime

date_start = datetime(2026, 2, 20, 12, 0, 0)
date_end = datetime(2026, 2, 21, 12, 0, 0)

difference = date_end - date_start

print(difference.total_seconds())
