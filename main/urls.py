from django.urls import path
from . import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('profil/', views.profil, name='profil'),
    path('ekstrakulikuler/', views.ekstrakulikuler, name='ekstrakulikuler'),
    path('berita/', views.berita, name='berita'),
    path('galeri/', views.galeri, name='galeri'),
    path('jurusan/<int:jurusan_id>/', views.jurusan_detail, name='jurusan_detail'),
    path('berita/<int:berita_id>/', views.berita_detail, name='berita_detail'),
]
