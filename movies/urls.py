from django.urls import path
from movies import views
# movies/ root
# movies/1/details

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
