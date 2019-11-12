from .models import OEM
from rest_framework import serializers


class OEMSerializer(serializers.ModelSerializer):
    class Meta:
        model = OEM
        fields = ['id', 'name']