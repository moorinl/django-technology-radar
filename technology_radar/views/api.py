from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from technology_radar.models import Area, Status, Blip, Radar
from technology_radar.serializers import (
    AreaSerializer, StatusSerializer, BlipSerializer, RadarSerializer)


__all__ = ['AreaListView', 'StatusListView', 'RadarListView',
           'RadarDetailView', 'BlipListView', 'BlipDetailView']


class AreaListView(APIView):
    def get(self, request, format=None):
        queryset = Area.objects.all()
        serializer = AreaSerializer(queryset, many=True)
        return Response(serializer.data)


class StatusListView(APIView):
    def get(self, request, format=None):
        queryset = Status.objects.all()
        serializer = StatusSerializer(queryset, many=True)
        return Response(serializer.data)


class RadarListView(APIView):
    def get(self, request, format=None):
        queryset = Radar.objects.all()
        serializer = RadarSerializer(queryset, many=True)
        return Response(serializer.data)


class RadarDetailView(APIView):
    def get(self, request, pk, format=None):
        obj = get_object_or_404(Radar, pk=pk)
        serializer = RadarSerializer(obj)
        return Response(serializer.data)


class BlipListView(APIView):
    def get(self, request, format=None):
        queryset = Blip.objects.all()
        serializer = BlipSerializer(queryset, many=True)
        return Response(serializer.data)


class BlipDetailView(APIView):
    def get(self, request, pk, format=None):
        obj = get_object_or_404(Blip, pk=pk)
        serializer = BlipSerializer(obj)
        return Response(serializer.data)
