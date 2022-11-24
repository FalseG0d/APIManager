from rest_framework.response import Response
from rest_framework.decorators import api_view

from .scraper import medium_Scraper

# Create your views here.
    
@api_view(['GET'])
def scrape(request):
    medium_url = request.GET.get('medium')

    return Response(
        medium_Scraper(medium_url)
        )