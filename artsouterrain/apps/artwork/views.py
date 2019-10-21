from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response

from artsouterrain.apps.artwork.models import Partner, PartnerType
from . import serializers


class PartnerViewSet(viewsets.ModelViewSet):

    queryset = Partner.objects.all()
    filter_fields = ('partner_type', 'partner_type__key', )
    permission_classes = ()

    def get_serializer_class(self):
        return serializers.PartnerSerializer

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


class PartnerTypeViewSet(viewsets.ModelViewSet):

    queryset = PartnerType.objects.all()
    filter_fields = '__all__'
    permission_classes = ()

    def get_serializer_class(self):
        return serializers.PartnerTypeSerializer

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
