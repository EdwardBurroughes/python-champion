from datetime import datetime, timezone
import zoneinfo
from zoneinfo import ZoneInfo

# python 3.9 datetimes timezone aware
print(datetime.now(tz=timezone.utc))
# can use zoneinfo working with timezones more convenient
# pulls timezones from Internet Assigned Numbers Authority database
print(datetime.now(tz=ZoneInfo("Europe/Oslo")))
# # to list all available time zones ->
print(zoneinfo.available_timezones())
# work out for time zone in 'Indian/Mauritius'
tz = ZoneInfo("Indian/Mauritius")
now = datetime.now(tz=tz)
print(now)

