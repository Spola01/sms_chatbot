import datetime
import pytz # pip install pytz

AUSTIN_TZ = pytz.timezone("America/Chicago")

def is_off_hours() -> bool:
now = datetime.datetime.now(AUSTIN_TZ)
weekday = now.weekday() # 0=Mon
hour = now.hour

# Clinic hours: Mon–Fri 9–17, Sat 9–13, Sun closed
if weekday == 6: # Sunday
return True
if weekday == 5 and not (9 <= hour < 13):
return True
if weekday < 5 and not (9 <= hour < 17):
return True
return False