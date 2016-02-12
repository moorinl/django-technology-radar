import factory

from technology_radar import models


class RadarFactory(factory.DjangoModelFactory):
    name = 'Moor Interactive'

    class Meta:
        model = models.Radar


class BlipFactory(factory.DjangoModelFactory):
    area = 'techniques'
    radar = factory.SubFactory(RadarFactory)
    status = 'access'
    name = 'BEM'
    body = 'Block, element and modifiers.'

    class Meta:
        model = models.Blip
