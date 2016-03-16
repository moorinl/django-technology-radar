from django import template

from technology_radar.models import Area, Status


register = template.Library()


@register.assignment_tag
def get_areas():
    return Area.objects.all()


@register.assignment_tag
def get_statuses():
    return Status.objects.all()


@register.assignment_tag
def get_radar_blips_by_area_status(radar, area, status):
    """
    Get radar blips by area status.
    """
    return radar.get_blips_by_area_status(area, status)
