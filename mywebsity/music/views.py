from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy
from .models import Album
from music.forms import RegistroForm



class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):

    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('index')

class RegistroUsuario(CreateView):
    model = User
    template_name = 'music/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('index')











'''
from django.shortcuts import render, get_object_or_404
from music.models import Album, Song

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
#    html = ''
#    for album in all_albums:
#        url = '/music/' + str(album.id) + '/'
#        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return render(request, 'music/index.html', context)

def detail(request, album_id):
#    try:
#        album = Album.objects.get(pk=album_id)
#    except Album.DoesNotExist:
#        raise Http404 ("Album does not exist")
#    return render(request, 'music/detail.html', {'album': album,})
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})
'''