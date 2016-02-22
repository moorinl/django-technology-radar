from autoslug import AutoSlugField

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from simple_history.models import HistoricalRecords


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Area(models.Model):
    name = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Status(models.Model):
    name = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Radar(TimeStampedModel):
    name = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class BlipManager(models.Manager):
    def by_area(self, area):
        return self.filter(area__slug=area)

    def by_status(self, status):
        return self.filter(status__slug=status)


@python_2_unicode_compatible
class Blip(TimeStampedModel):
    area = models.ForeignKey('Area', related_name='blips')
    radar = models.ForeignKey('Radar', related_name='blips')
    status = models.ForeignKey('Status', related_name='blips')
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    body = models.TextField()
    history = HistoricalRecords()
    objects = BlipManager()

    def __str__(self):
        return self.name
