import os
import sys
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_recommender.settings')
django.setup()

from movies.models import Movie
from django.contrib.auth.models import User

# Sample movies data
movies_data = [
    {
        'title': 'The Shawshank Redemption',
        'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
        'genres': 'Drama, Crime',
        'release_date': '1994-10-14',
        'rating': 4.8
    },
    {
        'title': 'The Godfather',
        'description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
        'genres': 'Crime, Drama',
        'release_date': '1972-03-24',
        'rating': 4.7
    },
    {
        'title': 'The Dark Knight',
        'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
        'genres': 'Action, Crime, Drama',
        'release_date': '2008-07-18',
        'rating': 4.7
    },
    {
        'title': 'Inception',
        'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
        'genres': 'Action, Adventure, Sci-Fi',
        'release_date': '2010-07-16',
        'rating': 4.6
    },
    {
        'title': 'Pulp Fiction',
        'description': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
        'genres': 'Crime, Drama',
        'release_date': '1994-10-14',
        'rating': 4.6
    },
    {
        'title': 'The Matrix',
        'description': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
        'genres': 'Action, Sci-Fi',
        'release_date': '1999-03-31',
        'rating': 4.5
    },
    {
        'title': 'Forrest Gump',
        'description': 'The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other historical events unfold through the perspective of an Alabama man with an IQ of 75.',
        'genres': 'Drama, Romance',
        'release_date': '1994-07-06',
        'rating': 4.5
    },
    {
        'title': 'Star Wars: Episode V - The Empire Strikes Back',
        'description': 'After the Rebels are brutally overpowered by the Empire on their newly established base, Luke Skywalker begins Jedi training with Yoda while his friends are pursued by Darth Vader.',
        'genres': 'Action, Adventure, Fantasy',
        'release_date': '1980-05-21',
        'rating': 4.5
    },
    {
        'title': 'The Lord of the Rings: The Return of the King',
        'description': 'Gandalf and Aragorn lead the World of Men against Sauron\'s army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.',
        'genres': 'Action, Adventure, Drama',
        'release_date': '2003-12-17',
        'rating': 4.5
    },
    {
        'title': 'Fight Club',
        'description': 'An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.',
        'genres': 'Drama',
        'release_date': '1999-10-15',
        'rating': 4.5
    }
]

# Create movies
for movie_data in movies_data:
    movie = Movie(
        title=movie_data['title'],
        description=movie_data['description'],
        genres=movie_data['genres'],
        release_date=datetime.strptime(movie_data['release_date'], '%Y-%m-%d').date(),
        rating=movie_data['rating']
    )
    movie.save()
    print(f'Created movie: {movie.title}')

print('\nSuccessfully added initial movie data!')
