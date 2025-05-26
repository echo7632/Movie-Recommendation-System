from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('genre/<str:genre_name>/', views.genre_movies, name='genre_movies'),
    path('search/', views.search, name='search'),
    path('rate/<int:movie_id>/', views.rate_movie, name='rate_movie'),
    path('recommendations/', views.recommendations, name='recommendations'),
]
