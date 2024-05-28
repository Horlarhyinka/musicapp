from django.urls import path
from .views import ListMusicView, AddMusicView, DeleteMusicView, UpdateeMusicView

urlpatterns = [
    path("", ListMusicView.as_view(), name="Get Musics"),
    path("", AddMusicView.as_view(), name="add music"),
    path("<int:id>", DeleteMusicView.as_view(), name="delete music"),
    path("<int:id>", UpdateeMusicView.as_view(), name="update music"),
    
]

