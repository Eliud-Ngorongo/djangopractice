from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
      {
        'Genre': "Comedy", 
        'Year':2002,
        'Title':"Mr Bones"
      },
      {
        'Genre': "Action", 
        'Year':1984,
        'Title':"Rambo"
      }, 
      {
        'Genre': "Crime Film", 
        'Year' :1983,
        'Title':"Scarface"},  
    
    ]
    }

name = {
    'names': ['Eliud', 'Njenga']
}


def movies(request):
    return render(request, 'movies/movies.html', data)


def home(request):
    return HttpResponse("This here is a home page")


def names(request):
    return render(request, 'movies/names.html', name)
