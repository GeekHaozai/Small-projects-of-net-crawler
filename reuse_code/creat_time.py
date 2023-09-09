import datetime
from datetime import timedelta

# start = datetime.datetime(2015, 1, 1, 0, 0, 0)
# end = datetime.datetime(2023, 1, 1, 0, 0, 0)
#
# while start <= end:
#     end_hour = start + timedelta(hours=1)
#     print(start.strftime("%Y-%m-%d-%H"), "-", end_hour.strftime("%Y-%m-%d-%H"))
#     start = end_hour

# while start <= end:
#     end_hour = start + timedelta(hours=1)
#     start_time = start.strftime("%Y-%m-%d-%H")
#     end_time = end_hour.strftime("%Y-%m-%d-%H")
#     time = f"custom:{start_time}:{end_time}"
#     print(time)
#     start = end_hour

#
# while start < end:
#     if start.hour == 8:
#         print(start.strftime("%Y-%m-%d-%H"), "-", (start + timedelta(hours=1)).strftime("%Y-%m-%d-%H"))
#
#     start += timedelta(hours=1)

#天数
start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2023, 1, 1)

while start.date() <= end.date():
    end_day = start + timedelta(days=1)
    print(start.strftime("%Y-%m-%d"), "-", end_day.strftime("%Y-%m-%d"))
    start = end_day