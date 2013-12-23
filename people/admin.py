from django.contrib import admin
from .models import Individual, ChurchGroup, Membership


class MembershipInline(admin.TabularInline):
    model= Membership
    extra= 1
    
    
class ChurchGroupAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)    


class IndividualAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {
       'last_name': ('last_name',),
    }
    
    inlines = (MembershipInline,)  

#     inlines = [
#                IndividualInline, ChurchGroupMembershipInline
#                ]

    list_display = ('last_name', 'first_name',)
    list_filter = ('last_name', 'first_name',)

admin.site.register(Individual, IndividualAdmin)
admin.site.register(ChurchGroup, ChurchGroupAdmin)