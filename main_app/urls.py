from django.urls import path, reverse
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('songs/', views.songs_index, name='index'),
  path('songs/<int:song_id>', views.songs_detail, name='detail'),
  path('songs/create', views.SongCreate.as_view(), name='songs_create'),
  path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),
  path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='songs_delete'),
  path('songs/<int:song_id>/add_performance/', views.add_performance, name='add_performance'),
  # added from slack
  path('books/', views.BookList.as_view(), name='books_index'),
  path('books/<int:pk>/', views.BookDetail.as_view(), name='books_detail'),
  path('books/create/', views.BookCreate.as_view(), name='books_create'),
  path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
  path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),
  # from the lecture notes
  path('songs/<int:song_id>/assoc_book/<int:book_id>/', views.assoc_book, name='assoc_book'),
  path('accounts/signup/', views.signup, name='signup'),
]