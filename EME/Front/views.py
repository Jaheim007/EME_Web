from django.shortcuts import render
from Front.models import Banner

# Create your views here.
def index(request):
    banners = Banner.objects.all() 
    return render(request, "pages/index.html" , locals())

def about(request):
    return render(request, "pages/about.html" , locals())

def contact(request):
    return render(request, "pages/contact.html" , locals())

def sermon(request):
    return render(request, "pages/sermons.html" , locals())