from django.contrib import admin
from .models import Album
from .models import Song,Video,Users

# Register your models here.
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Video)
admin.site.register(Users)