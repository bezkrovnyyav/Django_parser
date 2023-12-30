from django.contrib import admin
from .models import UserInfo



class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'email']


admin.site.register(UserInfo, UserInfoAdmin)
