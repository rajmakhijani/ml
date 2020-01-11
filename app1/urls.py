from django.urls import path
from .views import CSV

urlpatterns = [
    path('csv/',CSV,name='csv')
]
