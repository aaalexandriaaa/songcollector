from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Song, Book
from .forms import PerformanceForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def songs_index(request):
  songs = Song.objects.filter(user=request.user)
  return render(request, 'songs/index.html', {'songs': songs})

@login_required  
def songs_detail(request, song_id):
  song = Song.objects.get(id=song_id)
  books_song_doesnt_have = Book.objects.exclude(id__in=song.books.all().values_list('id'))
  performance_form = PerformanceForm()
  return render(request, 'songs/detail.html', {
    'song': song, 'performance_form': performance_form,
    'books': books_song_doesnt_have
    })

@login_required
def add_performance(request, song_id):
  form = PerformanceForm(request.POST)
  if form.is_valid():
    new_performance = form.save(commit=False)
    new_performance.song_id = song_id
    new_performance.save()
  return redirect('detail', song_id = song_id)

class SongCreate(LoginRequiredMixin, CreateView):
  model = Song
  fields = ('name', 'composer', 'period')
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class SongUpdate(LoginRequiredMixin, UpdateView):
  model = Song
  fields = ['name', 'composer', 'period']

class SongDelete(LoginRequiredMixin, DeleteView):
  model = Song
  success_url = '/songs/'

class BookList(LoginRequiredMixin, ListView):
  model = Book

class BookDetail(LoginRequiredMixin, DetailView):
  model = Book

class BookCreate(LoginRequiredMixin, CreateView):
  model = Book
  fields = ['name', 'publisher', 'author']

class BookUpdate(LoginRequiredMixin, UpdateView):
  model = Book
  fields = ['name', 'publisher', 'author']

class BookDelete(LoginRequiredMixin, DeleteView):
  model = Book
  success_url = '/books/'

@login_required
def assoc_book(request, song_id, book_id):
  Song.objects.get(id=song_id).books.add(book_id)
  return redirect('detail', song_id=song_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)