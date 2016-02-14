from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template import loader

from reportlab.pdfgen import canvas

from rest_framework.response import Response
from rest_framework.views import APIView

from technology_radar.models import Area, Status, Blip, Radar
from technology_radar.serializers import (
    AreaSerializer, StatusSerializer, BlipSerializer, RadarSerializer)


__all__ = ['ApiAreaListView', 'ApiStatusListView', 'ApiRadarListView',
           'ApiRadarDetailView', 'ApiBlipListView', 'ApiBlipDetailView',
           'index', 'radar_detail', 'radar_detail_pdf', 'area_detail',
           'blip_detail']


class ApiAreaListView(APIView):
    def get(self, request, format=None):
        queryset = Area.objects.all()
        serializer = AreaSerializer(queryset, many=True)
        return Response(serializer.data)


class ApiStatusListView(APIView):
    def get(self, request, format=None):
        queryset = Status.objects.all()
        serializer = StatusSerializer(queryset, many=True)
        return Response(serializer.data)


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


def radar_detail_pdf(request, radar):
    radar_obj = get_object_or_404(Radar, slug=radar)  # noqa

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="radar.pdf"'

    # Create the PDF object, using the response object as its "file."
    pdf = canvas.Canvas(response)

    # Close the PDF object cleanly, and we're done.
    pdf.showPage()
    pdf.save()
    return response


def area_detail(request, radar, area):
    radar_obj = get_object_or_404(Radar, slug=radar)
    area_obj = get_object_or_404(Area, slug=area)
    blips = Blip.objects.filter(radar=radar_obj, area=area_obj)
    template = loader.get_template('technology_radar/area.html')
    context = {
        'radar': radar_obj,
        'area': area_obj,
        'blips': blips
    }
    return HttpResponse(template.render(context, request))


def blip_detail(request, radar, area, blip):
    blip_obj = get_object_or_404(Blip, slug=blip)
    area_obj = get_object_or_404(Area, slug=area)  # noqa
    if blip_obj.radar.slug != radar:
        raise Http404
    radar_obj = get_object_or_404(Radar, slug=radar)
    template = loader.get_template('technology_radar/blip.html')
    context = {
        'radar': radar_obj,
        'blip': blip_obj
    }
    return HttpResponse(template.render(context, request))
