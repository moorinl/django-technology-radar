import factory

from technology_radar import models


class AreaFactory(factory.DjangoModelFactory):
    name = 'Tools'

    class Meta:
        model = models.Area


class StatusFactory(factory.DjangoModelFactory):
    name = 'Access'

    class Meta:
        model = models.Status


class RadarFactory(factory.DjangoModelFactory):
    name = 'Moor Interactive'

    class Meta:
        model = models.Radar


class BlipFactory(factory.DjangoModelFactory):
    area = factory.SubFactory(AreaFactory)
    radar = factory.SubFactory(RadarFactory)
    status = factory.SubFactory(StatusFactory)
    name = 'BEM'
    body = 'Block, element and modifiers.'

    class Meta:
        model = models.Blip
