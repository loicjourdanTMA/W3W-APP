from django.http import JsonResponse

def coordinates_view(request):
    if request.method == 'POST':
        # Process the incoming data (coordinates)
        # Let's assume you're sending JSON with latitude and longitude
        try:
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')

            # You can do further processing or validation here
            return JsonResponse({'latitude': latitude, 'longitude': longitude})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)  # If method isn't POST
