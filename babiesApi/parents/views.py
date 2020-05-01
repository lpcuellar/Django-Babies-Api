from django.shortcuts import render

from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from babies.models import Baby
from parents.models import Parent
from babies.serializers import BabySerializer
from parents.serializers import ParentSerializer


# Create your views here.
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ParentPermission',
            permission_configuration={
                'base': {
                    'create': False,
                    'list': False,
                },
                'instance': {
                    'retrieve': False,
                    'destroy': False,
                    'update': False,
                    'partial_update': False,
                    'babies': True
                }
            }
        ),
    )

    @action(detail=True, methods=['get'])
    def babies(self, request, pk=None):
        parent = self.get_object().parent
        parentBabies = []

        for baby in Baby.objects.filter(parent=parent):
            parentBabies.append(BabySerializer(baby).data)
        
        return Response(parentBabies)