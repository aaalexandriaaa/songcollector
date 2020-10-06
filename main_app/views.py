from django.shortcuts import render

# # Class Instantiation
# class Song:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, composer, period, multipart):
#     self.name = name
#     self.composer = composer
#     self.period = period
#     self.multipart = multipart

# songs = [
#   Song('Sonata No. 1 in C', 'Mozart', 'classical', True),
#   Song('Pathétique Sonata', 'Beethoven', 'classical', True),
#   Song('Fugue No 2 from Well-Tempered Clavier', 'Bach', 'Baroque', False)
# ]


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def songs_index(request):
  return render(request, 'songs/index.html', { 'songs': songs })