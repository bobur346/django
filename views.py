from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
#def homePage(request):
#    return HttpResponse("What's up!")
class HomePageView(TemplateView):
    template_name='home.html'
class AboutPageView(TemplateView):
    template_name='about.html'



