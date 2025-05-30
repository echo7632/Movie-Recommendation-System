# Generated by Django 5.2.1 on 2025-05-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_watch_time_userrating_watch_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_url',
            field=models.URLField(blank=True, help_text='URL to movie poster image', null=True),
        ),
    ]
