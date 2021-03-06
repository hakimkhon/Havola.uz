from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name', 'is_staff', 'email']
    list_display_links = list_display # ['id','first_name', 'last_name']
    readonly_fields = ['password']
    fieldsets = (
    # fields = ['first_name', 'last_name', 'is_staff', 'password']
    # list_filter = ['first_name']
    # list_editable = ['first_name', 'last_name', 'email']
    # search_fields = ['first_name']
        ('Personal Information', {
            "fields": (
                ('first_name', 'last_name'),
            ),
        }),
        ('Credentials', {
            "fields": (
                'email', 'password'
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff', 'is_superuser'
            ),
            'classes': ('collapse',),
        }),
    )
    

admin.site.register(User, UserAdmin)

