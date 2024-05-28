from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics, status
from .models import Music
from .serializers import MusicSerializer
from rest_framework.response import Response
import json

music_placeholder = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

class ListMusicView(generics.ListCreateAPIView):
    lookup_field = "id"
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    def create(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, IsAdminUser]
        self.check_permissions(request=request)
        name = request.data.get("name")
        artist = request.data.get("artist")
        data = {"name": name, "artist": artist, "url": music_placeholder}
        music_serializer = MusicSerializer(data=data)
        music_serializer.is_valid(raise_exception=True)
        music = music_serializer.save()
        return Response(music_serializer.data, status=status.HTTP_201_CREATED)


class AddMusicView(generics.CreateAPIView):
    serializer_class = MusicSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Music.objects.all()

class DeleteMusicView(generics.RetrieveDestroyAPIView):
    serializer_class = MusicSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Music.objects.all()

class UpdateeMusicView(generics.UpdateAPIView):
    serializer_class = MusicSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Music.objects.all()

