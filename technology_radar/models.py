from autoslug import AutoSlugField

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from simple_history.models import HistoricalRecords


RADAR_AREAS = getattr(settings, 'RADAR_AREAS', (
    ('techniques', _('Techniques')),
    ('tools', _('Tools')),
    ('platforms', _('Platforms')),
    ('languages_frameworks', _('Languages & Frameworks'))
))

RADAR_STATUSSES = getattr(settings, 'RADAR_STATUSSES', (
    ('access', _('Access')),
    ('trial', _('Trial')),
    ('adopt', _('Adopt')),
    ('on_hold', _('On hold'))
))


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Radar(TimeStampedModel):
    name = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Blip(TimeStampedModel):
    area = models.CharField(max_length=32, choices=RADAR_AREAS)
    radar = models.ForeignKey('Radar', related_name='blips')
    status = models.CharField(max_length=16, choices=RADAR_STATUSSES)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    body = models.TextField()
    history = HistoricalRecords()

    def __str__(self):
        return self.name
