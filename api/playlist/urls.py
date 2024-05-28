from django.urls import path
from .views import ListCreateView, GetUpdateDeleteView, ListPublicPlaylisView, AddListTrackView, GetDeleteTrackView

urlpatterns = [
    path("", ListCreateView.as_view(), name="List/create view"),
    path("<int:id>", GetUpdateDeleteView.as_view(), name="get/update/delete view"),
    path("public", ListPublicPlaylisView.as_view(), name="get-public-playlists"),
    path("<int:id>/tracks/", AddListTrackView.as_view(), name="add-list-tracks"),
    path("tracks/<int:id>", GetDeleteTrackView.as_view(), name="get-delete-tracks"),

]
