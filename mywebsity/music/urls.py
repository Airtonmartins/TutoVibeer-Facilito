from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from django.contrib.auth.views import login,logout_then_login

app_name = 'music'
urlpatterns = [
    #url(r'^music/')
    #/music/

    url(r'^$',  login ,{'template_name':'music/login.html'}, name='login'),

    url(r'^logout/', logout_then_login, name='logout'),

    url(r'^music/$',login_required(views.IndexView.as_view()), name='index'),

    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()), name='detail'),


    url(r'^registrar/$', views.RegistroUsuario.as_view(), name='registrar'),

    # /music/<album_id>/favorite/

#    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    #/music/album/add/
    url(r'album/add/$', login_required(views.AlbumCreate.as_view()), name='album-add'),

    # /music/album/2/

    url(r'album/(?P<pk>[0-9]+)/$', login_required(views.AlbumUpdate.as_view()), name='album-update'),

    # /music/album/2/delete/

    url(r'album(?P<pk>[0-9]+)/delete/$', login_required(views.AlbumDelete.as_view()), name='album-delete'),



]