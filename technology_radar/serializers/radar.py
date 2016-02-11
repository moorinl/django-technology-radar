from rest_framework import serializers

from technology_radar.models import Blip, Radar


class BlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blip
        fields = ('id', 'area', 'status', 'name', 'body', 'created',
                  'modified')


class RadarSerializer(serializers.ModelSerializer):
    blips = BlipSerializer(many=True)

    class Meta:
        model = Radar
        fields = ('id', 'name', 'created', 'modified', 'blips')
