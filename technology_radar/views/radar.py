from rest_framework.response import Response
from rest_framework.views import APIView


from technology_radar.models import Radar
from technology_radar.serializers import RadarSerializer


__all__ = ['RadarListView']


class RadarListView(APIView):
    def get(self, request, format=None):
        qs = Radar.objects.all()
        ser = RadarSerializer(qs, many=True)
        return Response(ser.data)
