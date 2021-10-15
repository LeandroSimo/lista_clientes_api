from django.db.models import fields
from rest_framework import serializers
from core.models import Clientes

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'