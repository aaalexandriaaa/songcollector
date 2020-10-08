from django.contrib import admin
# import your models here
from .models import Song, Performance
# Register your models here
admin.site.register(Song)
admin.site.register(Performance)