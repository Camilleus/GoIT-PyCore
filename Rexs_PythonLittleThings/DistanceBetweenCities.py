import math

RADIUS = 6371.01
radians = math.radians

arccos = math.acos
sin = math.sin
cos = math.cos

lat1, lon1 = map(float, input(
    "What are coordinates of your first city? (latitude and longtitude)").split())
lat2, lon2 = map(float, input(
    "What are coordinates of your second city? (latitude and longtitude)").split())


lon1 = radians(lon1)
lon2 = radians(lon2)
lat1 = radians(lat1)
lat2 = radians(lat2)

distance = 6371.01 * arccos(sin(lat1) * sin(lat2) +
                            cos(lat1) * cos(lat2) * cos(lon1 - lon2))

print(distance, " kilometers")
