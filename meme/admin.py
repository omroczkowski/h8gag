from django.contrib import admin
from .models import Meme

# Register your models here.

class MemeAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'description', 'rank', 'category', 'date_added', 'meme_img']

admin.site.register(Meme, MemeAdmin)