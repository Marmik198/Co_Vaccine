from django.shortcuts import render
from .models import Maha1, Incidences
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.contrib.gis.geoip2 import GeoIP2
from django.http import HttpResponse
from .load_layer import run
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point



def map_home(request):
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    # 	ip = x_forwarded_for.split(',')[0]
    # else:
    # 	ip = request.META.get('REMOTE_ADDR')
    # g = GeoIP2()
    # (lat, lng) = g.lat_lon(ip)
    # template_name = 'index.html'
    # pnt = Incidences.objects.get(name ='KJSCE').location
    lat = 71.353201
    lng = 22.44288
    pnt = Point(lat, lng, srid=4326)
    inc_near = Incidences.objects.annotate(
        distance=Distance('location', pnt)
    ).order_by('distance').first()
    string = str(inc_near.location)
    near_lng = float(string[17:26])
    near_lat = float(string[26:35])
    print(near_lat)
    print(near_lng)
    print(inc_near)

    context = {
        'lng': lat,
        'lat': lng,
        'near_lat': near_lat,
        'near_lng': near_lng,
    }
    return render(request, 'geo/index.html', context)


def maha_datasets(request):
    names = serialize('geojson', Maha1.objects.all())
    return HttpResponse(names,content_type='json')

def point_datasets(request):
    points = serialize('geojson', Incidences.objects.all())
    return HttpResponse(points,content_type='json')
