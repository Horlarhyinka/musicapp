from django.db import models

# Create your models here.
class Music(models.Model):
    url = models.URLField(default="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    cover = models.URLField(default="https://wikisound.org/mastering/Audio-waveform-player/data/default_artwork/music_ph.png")
    def __str__(self) -> str:
        return f"{self.name} - {self.artist}"
    