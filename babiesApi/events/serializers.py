from rest_framework import serializers

from events.models import Event
from babies.serializers import BabySerializer


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id'
            'name',
            'actionType',
            'notes',
            'date',
            'baby'
        )

