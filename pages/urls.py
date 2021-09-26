# pages/urls.py
from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home') #Note the path '' represents the homepage. 
]