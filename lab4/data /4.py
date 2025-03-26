from datetime import datetime

date1 = datetime(2025, 2, 10, 12, 0, 0)  # Example date
date2 = datetime(2025, 2, 12, 14, 30, 0)  # Another example date

difference = abs((date2 - date1).total_seconds())

print("Difference in seconds:", difference)