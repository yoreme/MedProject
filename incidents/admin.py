from django.contrib import admin

from rangefilter.filter import DateRangeFilter

from .models import Incident

# Register your models here.
class IncidentAdmin(admin.ModelAdmin):
    list_display=('id','place','personal_number','description','action','ip_address','latitude','longitude','country_name','country_code','city','region','created_at')
    list_filter = ('country_name','city','region','personal_number',('created_at', DateRangeFilter),)
    list_display_links=('id','personal_number')
    search_fields=('email','personal_number',)
    ordering = ('created_at',)
    list_per_page=25

admin.site.register(Incident,IncidentAdmin)

admin.site.site_header = "Med Proj Admin Portal"
admin.site.site_title = "Med Proj Admin Portal"
admin.site.index_title = "Welcome to Med Proj Admin Portal"
