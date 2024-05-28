from django.db import models
from django.contrib.auth.models import User
from music.models import Music
# Create your models here.
class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} by {self.user.username}"

class Track(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.playlist.name}- {self.music.name}"