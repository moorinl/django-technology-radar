from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template import loader

from technology_radar.forms import SearchForm
from technology_radar.models import Area, Blip, Radar
from technology_radar.utils import (convert_queryset_to_alphabetically_dict,
                                    import_class)


__all__ = ['index', 'radar_detail', 'radar_blip_list', 'radar_detail_download',
           'area_detail', 'blip_detail']


def index(request):
    radars = Radar.objects.all()
    template = loader.get_template('technology_radar/index.html')
    context = {
        'radars': radars
    }
    return HttpResponse(template.render(context, request))


def radar_detail(request, radar):
    radar_obj = get_object_or_404(Radar, slug=radar)
    areas = Area.objects.all()
    template = loader.get_template('technology_radar/radar.html')
    context = {
        'radar': radar_obj,
        'areas': areas
    }
    return HttpResponse(template.render(context, request))


def radar_blip_list(request, radar):
    radar_obj = get_object_or_404(Radar, slug=radar)
    context = {}
    q = request.GET.get('q', None)
    is_valid = False
    blips = radar_obj.blips.all()
    if q:
        form = SearchForm(request.GET)
        if form.is_valid():
            is_valid = True
            blips = blips.filter(name__icontains=q)
            context['q'] = q
            template = loader.get_template(
                'technology_radar/radar_blip_list_results.html')
    else:
        form = SearchForm()
    if not is_valid:
        blips = convert_queryset_to_alphabetically_dict(blips)
        template = loader.get_template('technology_radar/radar_blip_list.html')
    context.update({
        'form': form,
        'radar': radar_obj,
        'blips': blips
    })
    return HttpResponse(template.render(context, request))


def radar_detail_download(request, radar):
    radar_obj = get_object_or_404(Radar, slug=radar)
    renderer = import_class(getattr(settings, 'TECHNOLOGY_RADAR_RENDER_CLASS',
                            'technology_radar.renderers.PDFRenderer'))()
    response = renderer.render(request, radar_obj)
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
