from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Movie, UserRating
from django.contrib.auth.models import User
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def home(request):
    query = request.GET.get('q')
    movies = Movie.objects.all().order_by('-rating')
    
    if query:
        movies = movies.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(genres__icontains=query)
        )
    
    # Get all unique genres from movies
    genres = set()
    for movie in Movie.objects.all():
        if movie.genres:
            genres.update(genre.strip() for genre in movie.genres.split(','))
    
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(movies, 12)  # 12 movies per page
    
    try:
        movies_page = paginator.page(page)
    except PageNotAnInteger:
        movies_page = paginator.page(1)
    except EmptyPage:
        movies_page = paginator.page(paginator.num_pages)
    
    return render(request, 'movies/home.html', {
        'movies': movies_page,
        'genres': sorted(genres),
        'query': query or ''
    })

@require_GET
def genre_movies(request, genre_name):
    movies = Movie.objects.filter(genres__icontains=genre_name).order_by('-rating')
    
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(movies, 12)  # 12 movies per page
    
    try:
        movies_page = paginator.page(page)
    except PageNotAnInteger:
        movies_page = paginator.page(1)
    except EmptyPage:
        movies_page = paginator.page(paginator.num_pages)
    
    return render(request, 'movies/genre.html', {
        'movies': movies_page,
        'genre': genre_name,
        'total_movies': movies.count()
    })

@require_GET
def search(request):
    query = request.GET.get('query', '')
    if query:
        # Search by title, description, and genres
        movies = Movie.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(genres__icontains=query)
        ).order_by('-rating')
    else:
        movies = Movie.objects.all().order_by('-rating')
    
    return render(request, 'movies/search_results.html', {
        'movies': movies,
        'query': query
    })

@login_required
def rate_movie(request, movie_id):
    if request.method == 'POST':
        rating = float(request.POST.get('rating'))
        movie = Movie.objects.get(id=movie_id)
        UserRating.objects.create(user=request.user, movie=movie, rating=rating)
        return redirect('home')
    return redirect('home')

def get_recommendations(user_id):
    # Get all ratings for this user
    user_ratings = UserRating.objects.filter(user_id=user_id)
    
    if not user_ratings.exists():
        return Movie.objects.all().order_by('-rating')[:10]
    
    # Calculate user's favorite genres
    user_genres = {}
    for rating in user_ratings:
        for genre in rating.movie.genres.split(', '):
            user_genres[genre] = user_genres.get(genre, 0) + rating.rating
    
    # Get similar users based on ratings and genres
    similar_users = UserRating.objects.filter(
        movie__in=user_ratings.values('movie'),
        user__is_superuser=False
    ).exclude(user_id=user_id)
    
    # Calculate similarity scores with genre and watch time weights
    user_matrix = []
    for user in similar_users.values('user').distinct():
        user_ratings = UserRating.objects.filter(user=user['user'])
        user_row = []
        for movie in Movie.objects.all():
            rating = user_ratings.filter(movie=movie).first()
            if rating:
                # Calculate weighted score based on rating, genre match, and watch time
                genre_score = 0
                for genre in movie.genres.split(', '):
                    genre_score += user_genres.get(genre, 0)
                
                watch_time_score = 0
                if rating.watch_time and movie.watch_time:
                    watch_time_score = min(rating.watch_time.total_seconds() / movie.watch_time.total_seconds(), 1)
                
                total_score = (rating.rating * 0.6) + (genre_score * 0.3) + (watch_time_score * 0.1)
                user_row.append(total_score)
            else:
                user_row.append(0)
        user_matrix.append(user_row)
    
    # Calculate cosine similarity with weighted scores
    similarity_scores = cosine_similarity(user_matrix)
    
    # Get recommendations based on similar users' ratings and preferences
    recommendations = []
    for i, score in enumerate(similarity_scores[0]):
        if score > 0.5:  # Only consider users with high similarity
            user_ratings = UserRating.objects.filter(user=similar_users[i].user)
            for rating in user_ratings:
                if not UserRating.objects.filter(user_id=user_id, movie=rating.movie).exists():
                    # Calculate recommendation score based on multiple factors
                    genre_score = 0
                    for genre in rating.movie.genres.split(', '):
                        genre_score += user_genres.get(genre, 0)
                    
                    watch_time_score = 0
                    if rating.watch_time and rating.movie.watch_time:
                        watch_time_score = min(rating.watch_time.total_seconds() / rating.movie.watch_time.total_seconds(), 1)
                    
                    total_score = (rating.rating * 0.6) + (genre_score * 0.3) + (watch_time_score * 0.1)
                    recommendations.append((rating.movie, total_score))
    
    # Sort recommendations by weighted score
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return [movie for movie, _ in recommendations[:10]]

@login_required
def recommendations(request):
    recommended_movies = get_recommendations(request.user.id)
    return render(request, 'movies/recommendations.html', {'movies': recommended_movies})
