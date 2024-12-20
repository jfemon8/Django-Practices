from django.shortcuts import render, redirect
from .models import Musician
from .forms import MusicianForm

# Create your views here.

def home(request):
    musicians = Musician.objects.prefetch_related('albums').order_by('-id')
    data = []
    for musician in musicians:
        for album in musician.albums.all():
            data.append({
                'id': musician.id,
                'musician_name': f"{musician.first_name} {musician.last_name}",
                'email': musician.email,
                'album_rating': album.rating,
                'instrument_type': musician.instrument_type,
                'album_name': album.album_name,
                'release_date': album.release_date,
                'album_id' : album.id,
            })
    return render(request, 'home.html', {'data':data})

def AddMusician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MusicianForm()
    return render(request, 'add_musician.html', {'form':form})

def EditMusician(request, id):
    musician = Musician.objects.get(pk=id)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'add_musician.html', {'form':form})

def DeleteMusician(request, id):
    musician = Musician.objects.get(pk=id).delete()
    return redirect('home')