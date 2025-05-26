import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_recommender.settings')
django.setup()

from django.contrib.auth.models import User

username = 'Vijay'
email = 'pulivijaysaketh@gmail.com'
password = 'A1b2c3#$'

try:
    User.objects.create_superuser(username, email, password)
    print(f'Successfully created superuser {username}')
except Exception as e:
    print(f'Error creating superuser: {str(e)}')
