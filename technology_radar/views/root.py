from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


__all__ = ['RootView']


class RootView(APIView):
    def get(self, request, format=None):
        return Response({
            'area-list': reverse(
                'api-area-list', request=request, format=format),
            'status-list': reverse(
                'api-status-list', request=request, format=format),
            'radar-list': reverse(
                'api-radar-list', request=request, format=format),
            'blip-list': reverse(
                'api-blip-list', request=request, format=format)
        })
