from django.urls import path
from . import views

urlpatterns = [
    path('locations/coordinates/', views.coordinates, name='coordinates'),  # New endpoint for coordinates
]
