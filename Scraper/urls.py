from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('medium/', views.scrape_medium, name="medium"),
    path('github/', views.scrape_github, name="github"),
    path('itch/', views.scrape_itch, name="itch"),
]
