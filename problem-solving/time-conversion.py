s = input()
if s.endswith("PM"):
    evening = True
else:
    evening = False
s = s.rstrip("PAM")
hour, minute, second = s.split(":")
hour = int(hour)
if evening and hour != 12:
    hour += 12
if not evening and hour == 12:
    hour = 0

hour = str(hour)
if len(hour) == 1:
    hour = "0" + hour
print(hour, minute, second, sep=":")
