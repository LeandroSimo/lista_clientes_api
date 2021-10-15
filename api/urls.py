from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'clientes/', views.CliestesList.as_view(), name='clientes-list'),

]