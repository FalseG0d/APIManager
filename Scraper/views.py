from django.shortcuts import render

# Create your views here.

def scrape(request):
    if request.user.is_authenticated:
        # game_Scraper()
        article_Scraper()
    return redirect('/')