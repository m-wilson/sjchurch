from django.contrib import admin

from documents.models import FilerDocumentFile

class FilerDocumentAdmin(admin.ModelAdmin):
    list_filter = 'date',
    list_display = 'title', 'date', 'document', 'category'
    fields = 'title', 'date', 'document', 'about', 'category'
     
    date_hierarchy = 'date'
    list_filter = ('category','date',)
    
admin.site.register(FilerDocumentFile, FilerDocumentAdmin)