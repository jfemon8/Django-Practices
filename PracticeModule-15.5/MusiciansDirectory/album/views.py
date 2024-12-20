from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album

# Create your views here.

def AddAlbum(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm()
    return render(request, 'add_album.html', {'form':form})

def EditAlbum(request, id):
    album = Album.objects.get(pk=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
    else:
        form = AlbumForm(instance=album)
    return render(request, 'add_album.html', {'form':form})

