from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    '''
    Custom User Model that defined in models.py
    well be registered and configured here.
    '''
    model = User
    list_display = ('email','is_superuser','is_active','is_staff')
    list_filter = ('email','is_superuser','is_active','is_staff')
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (

        ('Authentication',{'fields':('email','password',),},),
        ('Permisions',{'fields':('is_staff','is_active','is_superuser',),},),
        ('Groups Permissions',{'fields':('groups','user_permissions'),},),
        ('Logins',{'fields':('last_login',),},),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':(  
            'email','password1','password2','is_active','is_staff','is_superuser',),
        }
        ),
    )

admin.site.register(User,CustomUserAdmin)