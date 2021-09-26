# # pages/views.py
# from django.http import HttpResponse

# def homePageView(request):
#     return HttpResponse('Hello, World!')



# pages/views.py
from django.views.generic import TemplateView


class homePageView(TemplateView):
    template_name = 'home.html'

class helpView(TemplateView):
    template_name = 'help.html'