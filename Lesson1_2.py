seconds = input("Введите секунды :")
hour = (float(seconds) / 60) / 60
solid_hour = int(hour)
#print (solid_hour)
after_point_hour = int(hour % 1 * 10000000000)
#print(after_point_hour)
minutes = float(60*(after_point_hour)) / 10000000000
solid_minutes = int(minutes)
#print(solid_minutes)
after_point_seconds = int(minutes % 1 * 10000000000)
#print(after_point_seconds)
seconds_2 = int(((60*(after_point_seconds)) / 10000000000)+1)
solid_seconds_2 = int(seconds_2)
#print(solid_seconds_2)
print (solid_hour, solid_minutes, solid_seconds_2, sep=':')
