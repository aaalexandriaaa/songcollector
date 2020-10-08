from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Song
from .forms import PerformanceForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def songs_index(request):
  songs = Song.objects.all()
  return render(request, 'songs/index.html', {'songs': songs})
  
def songs_detail(request, song_id):
  song = Song.objects.get(id=song_id)
  performance_form = PerformanceForm()
  return render(request, 'songs/detail.html', {'song': song, 'performance_form': performance_form})
  
  def add_performance(request, song_id):
    form = PerformanceForm(request.POST)
    if form.is_valid():
      new_performance = form.save(commit=False)
      new_performance.song_id = song_id
      new_performance.save()
    return redirect('detail', song_id = song_id)

class SongCreate(CreateView):
  model = Song
  fields = '__all__'

class SongUpdate(UpdateView):
  model = Song
  fields = '__all__'

class SongDelete(DeleteView):
  model = Song
  success_url = '/songs/'