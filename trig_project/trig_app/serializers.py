from rest_framework import serializers
from .models import Denomination,Retailer

class DenominationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Denomination
        fields = ('denom_name','retailer')

class RetailerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Retailer
        fields = ('retail_name',)

