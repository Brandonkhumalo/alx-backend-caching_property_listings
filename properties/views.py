from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .utils import get_all_properties

@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    properties = get_all_properties()
    # Serialize manually for JsonResponse
    properties_list = [
        {
            'id': p.id,
            'title': p.title,
            'description': p.description,
            'price': str(p.price),
            'location': p.location,
            'created_at': p.created_at.isoformat(),
        }
        for p in properties
    ]
    return JsonResponse({'data': properties_list})  # ✅ Now returns a dict with "data"
