from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))
print(datetime.now(KST).strftime("%Y-%m-%d"))
