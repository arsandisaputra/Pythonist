s = "12:05:45AM"
jam = converted = int(s[:2])

if s[-2] == 'P':
    if jam != 12:
        converted += 12
else:
    if jam == 12:
        converted = 0

now = str(converted)
now = now.zfill(2)
print(now+s[2:8])
