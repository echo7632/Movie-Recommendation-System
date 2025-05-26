import os
import sys
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_recommender.settings')
django.setup()

from movies.models import Movie
from django.contrib.auth.models import User

# Additional movies with watch times
movies_data = [
    {
        'title': 'The Lord of the Rings: The Fellowship of the Ring',
        'description': 'A meek hobbit of the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.',
        'genres': 'Adventure, Drama, Fantasy',
        'release_date': '2001-12-19',
        'rating': 4.5,
        'watch_time': 178
    },
    {
        'title': 'The Matrix Reloaded',
        'description': 'Neo and the rebel leaders estimate that they have 72 hours until 250,000 probes discover Zion and destroy it and its inhabitants. During this, Neo must decide how he can save Trinity from a dark fate in his dreams.',
        'genres': 'Action, Sci-Fi',
        'release_date': '2003-05-15',
        'rating': 4.4,
        'watch_time': 138
    },
    {
        'title': 'The Matrix Revolutions',
        'description': 'The human city of Zion defends itself against the massive invasion of the machines as Neo fights to end the war at another front while also opposing the rogue Agent Smith.',
        'genres': 'Action, Sci-Fi',
        'release_date': '2003-11-05',
        'rating': 4.3,
        'watch_time': 129
    },
    {
        'title': 'The Dark Knight Rises',
        'description': 'Eight years after the Joker\'s reign of anarchy, Batman, with the help of the enigmatic Catwoman, is forced from his exile to save Gotham City from the brutal guerrilla terrorist Bane.',
        'genres': 'Action, Crime, Drama',
        'release_date': '2012-07-20',
        'rating': 4.5,
        'watch_time': 165
    },
    {
        'title': 'Interstellar',
        'description': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
        'genres': 'Adventure, Drama, Sci-Fi',
        'release_date': '2014-11-07',
        'rating': 4.6,
        'watch_time': 169
    },
    {
        'title': 'Inception',
        'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
        'genres': 'Action, Adventure, Sci-Fi',
        'release_date': '2010-07-16',
        'rating': 4.6,
        'watch_time': 148
    },
    {
        'title': 'The Prestige',
        'description': 'After a tragic accident, two stage magicians in 1890s London engage in a battle to create the ultimate illusion while sacrificing everything they have to outwit each other.',
        'genres': 'Drama, Mystery, Sci-Fi',
        'release_date': '2006-10-20',
        'rating': 4.5,
        'watch_time': 130
    },
    {
        'title': 'The Departed',
        'description': 'An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.',
        'genres': 'Crime, Drama, Thriller',
        'release_date': '2006-10-06',
        'rating': 4.5,
        'watch_time': 151
    },
    {
        'title': 'The Wolf of Wall Street',
        'description': 'Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government.',
        'genres': 'Biography, Comedy, Crime',
        'release_date': '2013-12-25',
        'rating': 4.4,
        'watch_time': 180
    },
    {
        'title': 'The Grand Budapest Hotel',
        'description': 'The adventures of Gustave H, a legendary concierge at a famous European hotel between the wars, and Zero Moustafa, the lobby boy who becomes his most trusted friend.',
        'genres': 'Adventure, Comedy, Crime',
        'release_date': '2014-02-27',
        'rating': 4.4,
        'watch_time': 99
    }
]

# Create movies
for movie_data in movies_data:
    movie = Movie(
        title=movie_data['title'],
        description=movie_data['description'],
        genres=movie_data['genres'],
        release_date=datetime.strptime(movie_data['release_date'], '%Y-%m-%d').date(),
        rating=movie_data['rating'],
        watch_time=timedelta(minutes=movie_data['watch_time'])
    )
    movie.save()
    print(f'Created movie: {movie.title}')

print('\nSuccessfully added more movies with watch times!')
