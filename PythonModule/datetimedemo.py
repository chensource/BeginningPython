from datetime import datetime

now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S %a,%b'))
print(type(now))

timestamp = now.timestamp()
print(timestamp)

cday = datetime.strptime('2016-07-25 00:29:57', '%Y-%m-%d %H:%M:%S')
print(cday)
