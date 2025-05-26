import os
import sys
import django
from django.db import transaction

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_recommender.settings')
django.setup()

from movies.models import Movie

# Movie posters from The Movie Database (TMDB)
poster_data = {
    "The Shawshank Redemption": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
    "The Godfather": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
    "The Dark Knight": "https://image.tmdb.org/t/p/w500/1hFGg5hzQHpyQV5UWrEaLHVWz7B.jpg",
    "The Godfather: Part II": "https://image.tmdb.org/t/p/w500/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg",
    "12 Angry Men": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
    "The Lord of the Rings: The Fellowship of the Ring": "https://image.tmdb.org/t/p/w500/6oom5QYQ2yQTMJaF879hmw8uI0x.jpg",
    "The Matrix Reloaded": "https://image.tmdb.org/t/p/w500/55sZYaA4UdM8PZqz0JZsZ711Wzj.jpg",
    "The Matrix Revolutions": "https://image.tmdb.org/t/p/w500/55sZYaA4UdM8PZqz0JZsZ711Wzj.jpg",
    "The Dark Knight Rises": "https://image.tmdb.org/t/p/w500/1hFGg5hzQHpyQV5UWrEaLHVWz7B.jpg",
    "Interstellar": "https://image.tmdb.org/t/p/w500/nBNZadXqJSdt05SHLqgT0HuC5Gm.jpg",
    "Inception": "https://image.tmdb.org/t/p/w500/nBNZadXqJSdt05SHLqgT0HuC5Gm.jpg",
    "The Prestige": "https://image.tmdb.org/t/p/w500/8kCt96K24eZ65H4sJd34M35C5fL.jpg",
    "The Departed": "https://image.tmdb.org/t/p/w500/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg",
    "The Wolf of Wall Street": "https://image.tmdb.org/t/p/w500/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg",
    "The Grand Budapest Hotel": "https://image.tmdb.org/t/p/w500/1G0dhYtq2h28d9F65T6LUo0aV8q.jpg"
}

@transaction.atomic
def add_posters():
    # Get all movies from the database
    all_movies = Movie.objects.all()
    
    for title, poster_url in poster_data.items():
        # Try to find the movie by exact title match
        movies = Movie.objects.filter(title__icontains=title)
        
        if movies.exists():
            # If multiple matches, use the first one
            movie = movies.first()
            movie.poster_url = poster_url
            movie.save()
            print(f"Added poster for: {title}")
        else:
            print(f"Movie not found: {title}")

if __name__ == '__main__':
    add_posters()
    print("\nSuccessfully added movie posters!")
