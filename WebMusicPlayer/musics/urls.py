from lib2to3.fixes.fix_input import context

from django.urls import path, include
from WebMusicPlayer.musics import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/', include([
        path('create/', views.create_album, name='create_album'),
        path('details/<int:pk>/', views.album_details, name='album_details'),
        path('edit/<int:pk>/', views.edit_album, name='edit_album'),
        path('delete/<int:pk>/', views.delete_album, name='delete_album'),
    ])),
    path('song/', include([
        path('create/', views.create_song, name='create_song'),
    ])),
]


