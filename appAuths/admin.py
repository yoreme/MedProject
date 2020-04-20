from django.contrib import admin
from django.http import HttpResponse
import csv
from datetime import datetime
from rangefilter.filter import DateRangeFilter

from .models import UserProfile,User,UserLoginLogoutActivity
# Register your models here.


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        """ Refer to comment on line 34"""
        # field_names = [field.name for field in meta.fields]
        field_names = ['First Name', 'Last Name', 'Phone Number', 'Email']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=medproject-user-{}.csv'.format(datetime.now())
        writer = csv.writer(response)

        writer.writerow(field_names)
        """ Commented this out to handle the logic better for making this export feature more generic"""
        # for obj in queryset:
        #     row = writer.writerow([getattr(obj, field) for field in field_names])

        users = User.objects.all().values_list('first_name', 'last_name', 'phone_no', 'email')
        for user in users:
            writer.writerow(user)

        return response

    export_as_csv.short_description = "Export as Csv"

class UserAdmin(admin.ModelAdmin):
    list_display=('id','username','email','first_name','last_name','phone_no','is_staff', 'is_active','created_at')
    list_filter = ('username','email','is_staff','is_active',('created_at', DateRangeFilter),)
    list_display_links=('id','email','phone_no')
    search_fields=('username','email','phone_no')
    ordering = ('created_at',)
    list_per_page=25

admin.site.register(User,UserAdmin)


admin.site.site_header = "Med Proj Admin Portal"
admin.site.site_title = "Med Proj Admin Portal"
admin.site.index_title = "Welcome to Med Proj Admin Portal"

admin.site.register(UserProfile)
admin.site.register(UserLoginLogoutActivity)

