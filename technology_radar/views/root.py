from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


__all__ = ['ApiRootView']


class ApiRootView(APIView):
    def get(self, request, format=None):
        return Response({
            'radar-list': reverse('radar-list', request=request, format=format)
        })
