from rest_framework import serializers

from artsouterrain.apps.artwork.models import Partner, PartnerType


class PartnerTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PartnerType
        fields = '__all__'


class PartnerSerializer(serializers.HyperlinkedModelSerializer):

    partner_type = PartnerTypeSerializer(many=False)

    class Meta:
        model = Partner
        fields = '__all__'
