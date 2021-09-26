# pages/urls.py
from django.urls import path
from .views import homePageView,helpView

urlpatterns = [
    path('', homePageView.as_view(), name='home'), #Note the path '' represents the homepage. #This pattern is almost identical to what we did in Chapter 2 with one major difference: when using Class-Based Views, you always add as_view() at the end of the view name.
    path('help/', helpView.as_view(), name='help')
]