from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView


from technology_radar.models import Blip, Radar
from technology_radar.serializers import BlipSerializer, RadarSerializer


__all__ = ['RadarListView', 'RadarDetailView', 'BlipListView',
           'BlipDetailView']


class RadarListView(APIView):
    def get(self, request, format=None):
        qs = Radar.objects.all()
        ser = RadarSerializer(qs, many=True)
        return Response(ser.data)


class RadarDetailView(APIView):
    def get(self, request, pk, format=None):
        obj = get_object_or_404(Radar, pk=pk)
        ser = RadarSerializer(obj)
        return Response(ser.data)


class BlipListView(APIView):
    def get(self, request, format=None):
        qs = Blip.objects.all()
        ser = BlipSerializer(qs, many=True)
        return Response(ser.data)


class BlipDetailView(APIView):
    def get(self, request, pk, format=None):
        obj = get_object_or_404(Blip, pk=pk)
        ser = BlipSerializer(obj)
        return Response(ser.data)
