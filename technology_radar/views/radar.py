from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader

from rest_framework.response import Response
from rest_framework.views import APIView


from technology_radar.models import Blip, Radar
from technology_radar.serializers import BlipSerializer, RadarSerializer


__all__ = ['ApiRadarListView', 'ApiRadarDetailView', 'ApiBlipListView',
           'ApiBlipDetailView', 'index', 'radar_detail', 'blip_detail']


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
    radar = get_object_or_404(Radar, slug=radar)
    template = loader.get_template('technology_radar/radar.html')
    context = {
        'radar': radar
    }
    return HttpResponse(template.render(context, request))


def blip_detail(request, radar, blip):
    radar = get_object_or_404(Radar, slug=radar)
    blip = get_object_or_404(Blip, slug=blip)
    template = loader.get_template('technology_radar/blip.html')
    context = {
        'radar': radar,
        'blip': blip
    }
    return HttpResponse(template.render(context, request))
