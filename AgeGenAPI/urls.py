from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.home),
    path('getAgeGen', views.upload_image),
    re_path(r'image/upload/', views.upload_image, name='upload_image'),
]
