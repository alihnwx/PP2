from datetime import datetime

current_datetime = datetime.now().replace(microsecond=0)

print("Datetime without microseconds:", current_datetime)