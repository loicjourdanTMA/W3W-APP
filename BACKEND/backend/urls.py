from django.urls import path
from . import views  # Import your views here

urlpatterns = [
    # Your other URL patterns
    path('http://192.168.1.197:3000/locations/coordinates/', views.coordinates_view, name='coordinates'),
]
