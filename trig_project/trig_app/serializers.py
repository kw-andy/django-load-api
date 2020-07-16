from rest_framework import serializers
from .models import Denomination,Retailer

class DenominationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Denomination
        fields = ('denom_name','retailer')

class RetailerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Retailer
        fields = ('retail_name')

class DenomRetailSerializer(serializers.HyperlinkedModelSerializer):
    retail_name = serializers.CharField(source='retailer.retail_name')
    retail_addr = serializers.CharField(source='retailer.retail_addr')

    class Meta:
        model = Denomination
        fields = ('denom_name', 'retail_name', 'retail_addr')