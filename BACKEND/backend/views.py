from django.http import JsonResponse
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the home page!")


def coordinates_view(request):
    data = {"message": "Coordinates endpoint"}
    return JsonResponse(data)
