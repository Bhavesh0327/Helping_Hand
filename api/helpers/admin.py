from django.contrib.gis.geos import Point

# https://code.djangoproject.com/ticket/11094
def WGS84_to_Google(latitude, longitude):
    pnt = Point(latitude, longitude, srid=4326)
    pnt.transform(900913)
    return pnt.coords

def location(obj):
    return str(obj.latitude) + ', ' + str(obj.longitude) 