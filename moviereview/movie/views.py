from gc import get_objects
from django.shortcuts import render,get_object_or_404
from .models import Movie

# Create your views here.

def home(request):
    searchTerm=request.GET.get('searchMovie')

    if searchTerm:
        movies=Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies=Movie.objects.all()

    
    return render(request,"home.html",{'searchTerm':searchTerm,'movies':movies})

def details(request,title):
    movie=get_object_or_404(Movie,title=title)
    return render(request,"detail.html",{"movie":movie})

