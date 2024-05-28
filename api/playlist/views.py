from rest_framework.views import APIView
from rest_framework import generics, status
from .models import Playlist, Track
from django.db.models import Q
from .serializers import PlaylistSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from music.models import Music
from .serializers import PlaylistSerializer, TrackSerializer
from music.serializers import MusicSerializer

class ListCreateView(generics.ListCreateAPIView):

    serializer_class = PlaylistSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Playlist.objects.filter(Q(is_public=True) | Q(user=self.request.user))
        else:
            return Playlist.objects.filter(is_public=True)
        
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_playlists = PlaylistSerializer(queryset, many=True)
        return Response(serialized_playlists.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request=request)
        name = request.data.get("name")
        description = request.data.get("description")
        is_public = request.data.get("is_public")
        data = {"name": name, "description": description, "is_public": is_public, "user": request.user.id}
        playlist_serializer = PlaylistSerializer(data=data)
        playlist_serializer.is_valid(raise_exception=True)
        playlist_serializer.save()
        return Response(playlist_serializer.data, status=status.HTTP_201_CREATED)
    
class ListPublicPlaylisView(generics.ListAPIView):
    queryset = Playlist.objects.filter(is_public=True)
    serializer_class = PlaylistSerializer
    
class GetUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    def retrieve(self, request, *args, **kwargs):
        id = self.kwargs["id"]
        if request.user == None:
            result = Playlist.objects.filter(Q(id=id) & Q(is_public=True))
        else:
            result = Playlist.objects.filter(Q(id=id) & (Q(is_public = True) | Q(user=request.user)))
        if len(result) == 0:
            return Response({"message": "playlist not found"}, status=status.HTTP_404_NOT_FOUND)
        target = result[0]
        serialized_playlist = PlaylistSerializer(target)
        return Response(serialized_playlist.data, status=status.HTTP_200_OK)


    def update(self, request, *args, **kwargs):
        id = kwargs["id"]
        try:
            target = Playlist.objects.get(id=kwargs.get("id"))
        except Playlist.DoesNotExist:
            return Response({"message": "playlist not found"}, status=status.HTTP_404_NOT_FOUND)
        if target.user != request.user:
            return Response({"message": "You cannot update this playlist"}, status=status.HTTP_401_UNAUTHORIZED)
        name = request.data.get("name")
        description = request.data.get("description")
        is_public = request.data.get("is_public")
        if name != None:
            target.name = name
        if description != None:
            target.description = description
        if is_public != None:
            target.is_public = is_public

        serialized = PlaylistSerializer(target)
        
        playlist_serializer = PlaylistSerializer(data=serialized.data)
        playlist_serializer.is_valid(raise_exception=True)
        playlist_serializer.save()
        return Response(playlist_serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        id = kwargs["id"]
        try:
            target = Playlist.objects.get(id=kwargs.get("id"))
        except Playlist.DoesNotExist:
            return Response({"message": "playlist not found"}, status=status.HTTP_404_NOT_FOUND)
        if target.user != request.user:
            return Response({"message": "You cannot delete this playlist"}, status=status.HTTP_401_UNAUTHORIZED) 
        target.delete()
        return Response({"message": "successful"}, status=status.HTTP_204_NO_CONTENT)
    
class AddListTrackView(generics.ListCreateAPIView):
    def get_queryset(self):
        return Track.objects.filter(Q(playlist__is_public=True) | Q(playlist__user = self.request.user))
    
    serializer_class = TrackSerializer


    def create(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        self.serializer_class = TrackSerializer
        music_id = request.data.get("music_id")
        if not music_id:
            return Response({"message": "music_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            music = Music.objects.get(id= music_id)
        except Music.DoesNotExist:
            return Response({"message": "music not found"}, status=status.HTTP_400_BAD_REQUEST)
        playlist_id = kwargs.get("id")
        try:
            playlist = Playlist.objects.get(id=playlist_id)
        except Playlist.DoesNotExist:
            return Response({"message": "playlist not found"}, status=status.HTTP_404_NOT_FOUND)
        data = {"playlist_id": playlist.pk, "music_id": music.pk}
        sequelized_track = TrackSerializer(data=data)
        sequelized_track.is_valid(raise_exception=True)
        sequelized_track.save()
        return Response(sequelized_track.data, status=status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        try:
            playlist = Playlist.objects.get(id=kwargs.get("id"))
        except Playlist.DoesNotExist:
            return Response({"message": "playlist not found"}, status=status.HTTP_404_NOT_FOUND)
        if not playlist.is_public and playlist.user != self.request.user:
            return Response({"message": "you cannot view tracks from this playlist"}, status=status.HTTP_401_UNAUTHORIZED)
        tracks = Track.objects.filter(playlist=playlist)
        context = self.get_serializer_context()
        context["exclude_playlist"] = True
        track_serializer = TrackSerializer(tracks, many=True, context=context)
        return Response(track_serializer.data, status=status.HTTP_200_OK)
    
class GetDeleteTrackView(generics.RetrieveDestroyAPIView):
    def retrieve(self, request, *args, **kwargs):
        try:
            track = Track.objects.get(id=kwargs.get("id"))
        except Track.DoesNotExist:
            return Response({"message": "Track not found"}, status=status.HTTP_404_NOT_FOUND)
        if not track.playlist.is_public and track.playlist.user != self.request.user:
            return Response({"message": "your do not have permission to view this track"}, status=status.HTTP_401_UNAUTHORIZED)
        sequelized_track = TrackSerializer(track)
        return Response(sequelized_track.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        track = Track.objects.get(id=kwargs.get("id"))
        if not track:
            return Response({"message": "track not found"}, status=status.HTTP_400_BAD_REQUEST)
        if not track.playlist.is_public and track.playlist.user != self.request.user:
            return Response({"message": "your do not have permission to delete this track"}, status=status.HTTP_401_UNAUTHORIZED)
        track.delete()
        return Response({"message": "successful"}, status=status.HTTP_204_NO_CONTENT)
