from rest_framework import serializers
from .models import Track, Playlist
from music.serializers import MusicSerializer
       
class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    music_id = serializers.IntegerField(write_only=True)
    playlist_id = serializers.IntegerField(write_only = True)

    music = MusicSerializer(read_only=True)
    playlist = PlaylistSerializer(read_only=True)

    class Meta:
        model = Track
        fields = ["music", "playlist", "playlist_id", "music_id", "id"]
    
    def to_representation(self, instance):
            representation = super().to_representation(instance)
            if self.context.get('exclude_playlist'):
                representation.pop('playlist')
            return representation