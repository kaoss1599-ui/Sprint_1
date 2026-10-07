line = '1h 45m,360s,25m,30m 120s,2h 60s'
time_list = line.split(',')
total_minutes = 0

for time in time_list:
    parts = time.split()
    for part in parts:
        if 'h' in part:
            minutes = int(part.replace('h', '')) * 60
        elif 'm' in part:
            minutes = int(part.replace('m', ''))
        elif 's' in part:
            minutes = int(part.replace('s', '')) // 60
        total_minutes += minutes

print(total_minutes)