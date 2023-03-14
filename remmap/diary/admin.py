from django.contrib import admin
from .models import Diary, Music


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    
    list_display = ("created_at", "updated_at", "title", "content")
    

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    
    list_display = ("title", "singer",)


