from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie
# Create your models here.


class MovieResource(ModelResource):
    class Meta:
        # returns an query it is known as lazy loading
        queryset = Movie.objects.all()

        resource_name = 'movies'
