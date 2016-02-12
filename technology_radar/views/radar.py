from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template import loader

from rest_framework.response import Response
from rest_framework.views import APIView


from technology_radar.models import RADAR_AREAS, Blip, Radar
from technology_radar.serializers import BlipSerializer, RadarSerializer


__all__ = ['ApiRadarListView', 'ApiRadarDetailView', 'ApiBlipListView',
           'ApiBlipDetailView', 'index', 'radar_detail', 'area_detail',
           'blip_detail']


class ApiRadarListView(APIView):
    def get(self, request, format=None):
        queryset = Radar.objects.all()
        serializer = RadarSerializer(queryset, many=True)
        return Response(serializer.data)


class ApiRadarDetailView(APIView):
    def get(self, request, pk, format=None):
        obj = get_object_or_404(Radar, pk=pk)
        serializer = RadarSerializer(obj)
        return Response(serializer.data)


class ApiBlipListView(APIView):
    def get(self, request, format=None):
        queryset = Blip.objects.all()
        serializer = BlipSerializer(queryset, many=True)
        return Response(serializer.data)


class ApiBlipDetailView(APIView):
    def get(self, request, pk, format=None):
        obj = get_object_or_404(Blip, pk=pk)
        serializer = BlipSerializer(obj)
        return Response(serializer.data)


def index(request):
    radars = Radar.objects.all()
    template = loader.get_template('technology_radar/index.html')
    context = {
        'radars': radars
    }
    return HttpResponse(template.render(context, request))


def radar_detail(request, radar):
    radar_obj = get_object_or_404(Radar, slug=radar)
    template = loader.get_template('technology_radar/radar.html')
    context = {
        'radar': radar_obj
    }
    return HttpResponse(template.render(context, request))


def area_detail(request, radar, area):
    if area not in dict(RADAR_AREAS):
        raise Http404
    radar_obj = get_object_or_404(Radar, slug=radar)
    blips = Blip.objects.filter(radar=radar_obj, area=area)
    template = loader.get_template('technology_radar/area.html')
    context = {
        'radar': radar_obj,
        'area': dict(RADAR_AREAS).get(area),
        'blips': blips
    }
    return HttpResponse(template.render(context, request))


def blip_detail(request, radar, area, blip):
    blip_obj = get_object_or_404(Blip, slug=blip)
    if area != blip_obj.area:
        raise Http404
    if blip_obj.radar.slug != radar:
        raise Http404
    radar_obj = get_object_or_404(Radar, slug=radar)
    template = loader.get_template('technology_radar/blip.html')
    context = {
        'radar': radar_obj,
        'blip': blip_obj
    }
    return HttpResponse(template.render(context, request))
