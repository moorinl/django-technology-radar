from rest_framework import serializers

from technology_radar.models import Radar


class RadarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radar
