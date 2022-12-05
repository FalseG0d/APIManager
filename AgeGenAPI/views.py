from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import ImageForm

from django.shortcuts import render

# from .AgeGenCalc import detect

# Create your views here.

def upload_image(request):
    data = {}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        data['form'] = form
 
        if form.is_valid():
            img_object = form.instance
            detect.printAgeGen(img_object)
            # print(img_object.image)
            # data['img_object'] = img_object.image
            form.save()
    else:
        form = ImageForm()
        data['form'] = form
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