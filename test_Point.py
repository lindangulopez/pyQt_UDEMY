import Point as pt

pt1 = pt.Point(3, 12, 4326)
pt2 = pt.Point(6, 16, 2200, 4326)

print(pt1.srs)
print(pt1.distance_to(pt2))
print(type(pt2))
print(pt2.get__units)
pt2.set__units("feet")