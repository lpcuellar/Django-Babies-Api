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
def evaluateParent(parent, obj, request):
    return parent.username == obj.parent.username
    

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': False,
                },
                'instance': {
                    'retrieve': 'babies.view_baby',
                    'destroy': 'babies.delete_baby',
                    'update': 'babies.change_baby',
                    'partial_update': 'baby.change_baby',
                    'events': evaluateParent
                }
            }
        ),
    )

    def perform_create(self, serializer):
        baby = serializer.save()
        parent.self.request.parent
        
        assign_perm('babies.view_baby', parent, baby)
        assign_perm('babies.delete_baby', parent, baby)
        assign_perm('babies.change_baby', parent, baby)
        
        return Response(serializer.data)

        @action(detail=True, methods=['get'])
        def events(self, request, pk=None):
            baby = self.get_object()
            babyEvents = []
            
            for events in Event.objects.filter(baby=baby):
                babyEvents.append(EventSerializer(event).data)
            
            return Response(babyEvents)