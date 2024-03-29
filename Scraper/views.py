from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render
from .scraper import medium_Scraper, github_Scraper, itch_Scraper

# Create your views here.

def home(request):

    return render(request,"scrape.html")

@api_view(['GET'])
def scrape_medium(request):
    medium_url = request.GET.get('url')

    return Response(
        medium_Scraper(medium_url)
        )

@api_view(['GET'])
def scrape_github(request):
    github_url = request.GET.get('url')

    return Response(
        github_Scraper(github_url)
        )


@api_view(['GET'])
def scrape_itch(request):
    itch_url = request.GET.get('url')

    return Response(
        itch_Scraper(itch_url)
        )