from django import template


register = template.Library()


@register.assignment_tag
def get_radar_blips_by_area(radar, area):
    return radar.get_blips_by_area(area)


@register.assignment_tag
def get_radar_blips_by_status(radar, status):
    return radar.get_blips_by_status(status)
