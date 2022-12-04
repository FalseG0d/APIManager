from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('medium/', views.scrape_medium),
    path('github/', views.scrape_github),
]
