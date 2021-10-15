from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from core.models import Clientes
from api.serializers import ClientesSerializer

class CliestesList(generics.ListCreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
   # permission_classes = [permissions.IsAuthenticated]