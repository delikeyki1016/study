import sys

hour, minute = [int(i) for i in sys.stdin.readline().split()]
taking = int(sys.stdin.readline().rstrip())

end_minute = minute + taking
if end_minute >= 60:
    add_hour = end_minute // 60
    hour += add_hour
    if hour >= 24:
        hour %= 24
    end_minute %= 60
print(hour, end_minute)