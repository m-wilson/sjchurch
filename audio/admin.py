from django.contrib import admin

from audio.models import FilerAudioFile

class FilerAudioAdmin(admin.ModelAdmin):
    list_filter = 'date',
    list_display = 'title', 'date', 'audiofile'
    fields = 'title', 'date', 'audiofile'
     
    date_hierarchy = 'date'
    
admin.site.register(FilerAudioFile, FilerAudioAdmin)