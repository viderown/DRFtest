from rest_framework import serializers

from api.models import Deal


class DealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deal
        fields = ['customer', 'item', 'total', 'quantity', 'date']