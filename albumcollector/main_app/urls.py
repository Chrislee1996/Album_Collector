# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('albums/', views.albums_index, name='albums_index'),
    path('albums/<int:album_id>/' , views.albums_show, name = 'albums_show')
]