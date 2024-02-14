
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()

    return render(request, 'movies/index.html', {'movies': movies})
    # output = ', '.join([m.title for m in movie])
    # SELECT * FROM movies_movie
    # Movie.objects.filter(releaseYear=1984)
    # # SELECT * FROM movies_moveie WHERE releaseYear=1984
    # Movie.objects.get(id=1)

    # return HttpResponse(output)


def detail(request, movie_id):
    # can use either id or pk # the get_list_or_404 makes it so we don't have to repeat writing try and catch statements
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
