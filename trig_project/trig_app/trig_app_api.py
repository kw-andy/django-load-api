from rest_framework import serializers,viewsets
from .models import Denomination

class DenomSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Denomination
        fields = ('denom_name','retailer')

class DenomViewSet(viewsets.ModelViewSet);
    queryset = Denomination.objects.all()
    serializer_class = DenomSerialiser        