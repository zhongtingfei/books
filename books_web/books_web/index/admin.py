from django.contrib import admin
from .models import *
# Register your models here.

# class Books_Users_Admin(admin.ModelAdmin):
#     pass
#

class UsersAdmin(admin.ModelAdmin):
    list_display = ['user_name','user_passwd','user_email']
    search_fields = ['user_name']


admin.site.register(Users,UsersAdmin)

admin.site.register(Books)