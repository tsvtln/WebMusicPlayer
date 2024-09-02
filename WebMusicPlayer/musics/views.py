from django.shortcuts import render

from WebMusicPlayer.common.session_decorator import session_decorator
from WebMusicPlayer.musics.models import Album
from WebMusicPlayer.settings import session


@session_decorator(session)
def index(request):
    albums = session.query(Album).all()
    context = {
        'albums': albums,
    }
    return render(request, 'common/index.html', context)

def create_album(request):
    return render(request, 'albums/create-album.html')

def edit_album(request, pk: int):
    return render(request, 'albums/edit-album.html')

def delete_album(request, pk: int):
    return render(request, 'albums/delete-album.html')

@session_decorator(session)
def album_details(request, pk: int):
    album = session.query(Album).filter(Album.id == pk).first()
    context = {
        "album": album,
    }
    return render(request, 'albums/album-details.html', context)

def create_song(request):
    return render(request, 'songs/create-song.html')