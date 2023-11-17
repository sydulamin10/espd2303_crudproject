from django.urls import path
from .views import read


urlpatterns = [
    path('read/<int:id>/', read, name='read')
]
