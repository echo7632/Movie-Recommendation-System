from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genres = models.CharField(max_length=200)
    release_date = models.DateField()
    rating = models.FloatField(default=0.0)
    watch_time = models.DurationField(null=True, blank=True, help_text="Movie duration in minutes")
    poster_url = models.URLField(null=True, blank=True, help_text="URL to movie poster image")
    
    def __str__(self):
        return self.title

    def get_duration(self):
        """Return movie duration in hours and minutes format"""
        if self.watch_time:
            minutes = self.watch_time.total_seconds() / 60
            hours = int(minutes // 60)
            remaining_minutes = int(minutes % 60)
            if hours > 0:
                return f"{hours}h {remaining_minutes}m"
            return f"{remaining_minutes}m"
        return "N/A"

class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    watch_time = models.DurationField(null=True, blank=True, help_text="Time spent watching the movie")
    
    class Meta:
        unique_together = ('user', 'movie')
    
    def __str__(self):
        return f"{self.user.username} rated {self.movie.title}: {self.rating}"
