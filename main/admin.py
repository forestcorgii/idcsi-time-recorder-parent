from django.contrib import admin

from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('employee_id', 'last_name', 'first_name', 'company', 'department')
    list_filter = ('employee_id',)
    fieldsets = (
        (None, {'fields': ('employee_id',)}),
        ('Personal info', {'fields': ('last_name', 'first_name', 'middle_name')}),
        ('Company Information', {'fields': ('site', 'company', 'department', 'project', 'schedule', 'active', 'admin')}),
    )

    search_fields = ('employee_id', 'first_name', 'last_name', 'department')
    ordering = ('employee_id',)
    list_filter = ('site', 'company', 'active', 'admin', 'department',)
    
admin.site.register(Profile, ProfileAdmin)
