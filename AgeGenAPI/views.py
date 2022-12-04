from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ImageModel

from django.shortcuts import render

from django.http import FileResponse

# Create your views here.

def upload_image(request):
    data = dict()
    if "GET" == request.method:
        return render(request, 'agegen.html', data)
    
    # process POST request
    files = request.FILES
    image = files.get("image")

    print(files)
    data["upload"] = image
    
    return render(request, 'agegen.html', data)


def home(request):
    context = {}
    return render(request,"agegen.html", context)

@api_view(['POST'])
def getAgeGen(request):
    img = request.FILES["input image"]
    
    context = {
        'upload': img.url,
    }

    return render(request,"agegen.html", context)

# @api_view(['GET'])
# def scrape_medium(request):
#     medium_url = request.GET.get('url')

#     return Response(
#         medium_Scraper(medium_url)
#         )

# @api_view(['GET'])
# def scrape_github(request):
#     github_url = request.GET.get('url')

#     return Response(
#         github_Scraper(github_url)
#         )