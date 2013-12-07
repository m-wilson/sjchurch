from django.contrib import admin
from .models import  Event, EventOrganiser, EventCategory, RecurringEvent, RecurringEventExclusion
# from .models import  Event, EventOrganiser, RecurringEvent, RecurringEventExclusion


class CategoryAdmin(admin.ModelAdmin): 
    search_fields = ('title',)
#     prepopulated_fields = {
#        'slug': ('title',)
#     }

class RecurringEventInline(admin.TabularInline):
    model = RecurringEvent
    extra = 1


class RecurringEventExclusionInline(admin.TabularInline):
    model = RecurringEventExclusion
    extra = 0
    
class OrganiserInline(admin.TabularInline):
    model = EventOrganiser
    extra = 1
    
class CategoryInline(admin.TabularInline):
    model = EventCategory
    extra = 1

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {
       'slug': ('title',)
    }
    inlines = (
        RecurringEventInline,
        RecurringEventExclusionInline,
        OrganiserInline,
        CategoryInline,
    )

    date_hierarchy = 'start'
    list_display = ('title', 'start',)
    list_filter = ('start', 'category', 'organiser')

admin.site.register(Event, EventAdmin)
