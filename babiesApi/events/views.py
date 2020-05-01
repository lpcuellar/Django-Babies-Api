from django.shortcuts import render

from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from babies.models import Baby
from events.models import Event
from babies.serializers import BabySerializer
from events.serializers import EventSerializer


# Create your views here.
def evaluateParent(parent, request):
    babyID = (request.POST).get('baby', 0)
    baby = Baby.objects.filter(pk=babyID)[0]
    return parent.username == obj.parent.username
    

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': evaluateParent,
                    'list': False,
                },
                'instance': {
                    'retrieve': 'events.view_event',
                    'destroy': 'events.delete_event',
                    'update': 'events.change_event',
                    'partial_update': 'event.change_event',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        event = serializer.save()
        parent.self.request.parent
        
        assign_perm('events.view_event', parent, event)
        assign_perm('events.delete_event', parent, event)
        assign_perm('events.change_event', parent, event)
        
        return Response(serializer.data)