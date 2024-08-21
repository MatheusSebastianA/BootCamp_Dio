import pytz
from datetime import datetime, timedelta

data = datetime.now(pytz.timezone("Europe/Oslo"))

print(data)