from django.urls import path

from .views import delete

urlpatterns = [
    path('delete/<int:id>/', delete, name='delete') #dynamic url
]
